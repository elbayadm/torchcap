import torch
from torch import nn
from torch.nn import functional as F


def ShowAttendAttention(query, attention):
    """
    Input:
        query: rnn hidden state (N, D)
        attention: region embeddings (N, D, W, H)
    Outpt:
        context : weighted sum of attended Regions
        attn_scores : weight assigned to each
    """
    bs, d, w, h = attention.size()
    attention = attention.contiguous().view(bs, d, -1)
    # print("Regions :", attention.size())
    # print("Query:", query.unsqueeze(1).size())
    score = torch.matmul(query.unsqueeze(1), attention).squeeze(1)
    # print('Scores:', score.size())
    normalized_score = F.softmax(score)
    # print('Attention scores:', normalized_score[0])
    # context = sum e_i a_i
    context = torch.matmul(normalized_score.unsqueeze(1),
                           attention.transpose(1, 2)).squeeze(1)
    # print('context:', context.size())
    return context, normalized_score.contiguous().view(bs, w, h)


class ShowAttendLSTM(nn.Module):
    def __init__(self, embedding, lstm_cell, attention, projection, logit):
        """
        inputs:
            E = word embedding size, D = rnn hidden size
            embedding: Word embedding layer (a lookup table) V x E
            lstm_cell: RNN LSMT cell dim(x) = E + D, dim(h) = D
            attention: Linear layer D x D
            projection: Linear layer (E + 2D) x D
            logit:      Linear layer D x V
        """
        super().__init__()
        self._embedding = embedding
        self._lstm_cell = lstm_cell
        self._attention = attention
        self._projection = projection
        self._logit = logit

    def forward(self, enc_img, input, init_states):
        """
        enc_img     : region embeddings a_1,...a_L
        input       : gt sequence of tokens
        inti_states : h_0, c_0 (obtained as MLP(avearge(a_i)))T
        """
        batch_size, max_len = input.size()
        logits = []
        states = init_states
        for i in range(max_len):
            tok = input[:, i:i+1]
            logit, states, _ = self._step(tok, states, enc_img)
            logits.append(logit)
        return torch.stack(logits, dim=1)

    def _step(self, tok, states, attention):
        h, c = states
        # print('initial states:', h.size(), c.size(), h[-1].size())
        context, attn_scores = step_attention(self._attention(h[-1]), attention)
        emb = self._embedding(tok).squeeze(1)
        x = torch.cat([emb, context], dim=1).unsqueeze(0)
        # print('Feeding to the RNN:', x.size())
        out, (h, c) = self._lstm_cell(x, (h, c))
        # print('LSTM outputs:', out.size(), h.size(), c.size(), out[-1].size())
        input_proj = torch.cat([emb, context, out[-1]], dim=1)
        output = self._projection(input_proj)
        # print('Final output size:', output.size())
        # logit = F.log_softmax(torch.mm(output, self._embedding.weight.t()))  # If using a single embedding matrix
        logit = F.log_softmax(self._logit(output))
        return logit, (h, c), attn_scores

    def decode_step(self, tok, states, attention):
        logit, states, attn = self._step(tok, states, attention)
        prob, out = logit.max(dim=1, keepdim=True)
        return out, prob, states, attn


class AdaptiveAttentionLSTM(nn.Module):
    def __init__(self, opt):
        super(AdaptiveAttentionLSTM, self).__init__()
        self.input_encoding_size = opt.input_encoding_size
        #self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size
        self.num_layers = opt.num_layers
        self.drop_prob_lm = opt.drop_prob_lm
        self.drop_x_lm = opt.drop_x_lm
        self.drop_sentinel = opt.drop_sentinel
        self.fc_feat_size = opt.fc_feat_size
        self.att_feat_size = opt.att_feat_size
        self.att_hid_size = opt.att_hid_size
        self.use_maxout = opt.use_maxout
        self.add_fc_img = opt.add_fc_img

        # Build a LSTM
        self.w2h = nn.Linear(self.input_encoding_size,
                             (4 + self.use_maxout) * self.rnn_size)
        self.v2h = nn.Linear(self.rnn_size,
                             (4 + self.use_maxout) * self.rnn_size)
        self.i2h = nn.ModuleList([nn.Linear(self.rnn_size,
                                            (4 + self.use_maxout) *
                                            self.rnn_size)
                                  for _ in range(self.num_layers - 1)])
        self.h2h = nn.ModuleList([nn.Linear(self.rnn_size,
                                            (4 + self.use_maxout) *
                                            self.rnn_size)
                                  for _ in range(self.num_layers)])

        # Layers for getting the fake region
        if self.num_layers == 1:
            self.r_w2h = nn.Linear(self.input_encoding_size, self.rnn_size)
            self.r_v2h = nn.Linear(self.rnn_size, self.rnn_size)
        else:
            self.r_i2h = nn.Linear(self.rnn_size, self.rnn_size)
        self.r_h2h = nn.Linear(self.rnn_size, self.rnn_size)


    def forward(self, xt, img_fc, state, step):
        """
        A standard LSTM where x_t = [w_t, img_fc]
        yields updated states (h_t, c_t) with drop(last_ht) and sentinel outout s_t
        """

        hs = []
        cs = []
        for L in range(self.num_layers):
            # c,h from previous timesteps
            prev_h = state[0][L]
            prev_c = state[1][L]
            # the input to this layer
            if L == 0:
                x = xt
                x = F.dropout(x, self.drop_x_lm, self.training)  # Maha to match Show&Tell
                if self.add_fc_img:
                    i2h = self.w2h(x) + self.v2h(img_fc)
                else:
                    if step:
                        i2h = self.w2h(x)
                    else:  # add the image only at t=0
                        i2h = self.w2h(x) + self.v2h(img_fc)
            else:
                x = hs[-1]
                x = F.dropout(x, self.drop_x_lm, self.training)
                i2h = self.i2h[L-1](x)

            all_input_sums = i2h+self.h2h[L](prev_h)

            sigmoid_chunk = all_input_sums.narrow(1, 0, 3 * self.rnn_size)
            sigmoid_chunk = F.sigmoid(sigmoid_chunk)
            # decode the gates
            in_gate = sigmoid_chunk.narrow(1, 0, self.rnn_size)
            forget_gate = sigmoid_chunk.narrow(1, self.rnn_size, self.rnn_size)
            out_gate = sigmoid_chunk.narrow(1, self.rnn_size * 2, self.rnn_size)
            # decode the write inputs
            if not self.use_maxout:
                in_transform = F.tanh(all_input_sums.narrow(1, 3 * self.rnn_size, self.rnn_size))
            else:
                in_transform = all_input_sums.narrow(1, 3 * self.rnn_size, 2 * self.rnn_size)
                in_transform = torch.max(\
                    in_transform.narrow(1, 0, self.rnn_size),
                    in_transform.narrow(1, self.rnn_size, self.rnn_size))
            # perform the LSTM update
            next_c = forget_gate * prev_c + in_gate * in_transform
            # gated cells form the output
            tanh_nex_c = F.tanh(next_c)
            next_h = out_gate * tanh_nex_c
            # -------------- Visual sentinel: get g_t & s_t = fake region
            if L == self.num_layers-1:
                if L == 0:
                    i2h = self.r_w2h(x) + self.r_v2h(img_fc)
                else:
                    i2h = self.r_i2h(x)
                n5 = i2h+self.r_h2h(prev_h)
                sentinel = F.sigmoid(n5) * tanh_nex_c

            cs.append(next_c)
            hs.append(next_h)

        # set up the decoder
        top_h = hs[-1]
        # top_h = F.dropout(top_h, self.drop_prob_lm, self.training)
        # sentinel = F.dropout(sentinel, self.drop_sentinel, self.training)
        state = (torch.cat([_.unsqueeze(0) for _ in hs], 0),
                 torch.cat([_.unsqueeze(0) for _ in cs], 0))
        return top_h, sentinel, state


class AdaptiveAttention(nn.Module):
    def __init__(self, opt):
        super(AdaptiveAttention, self).__init__()
        self.logger = opt.logger
        self.input_encoding_size = opt.input_encoding_size
        # self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size
        self.drop_prob_lm = opt.drop_prob_lm
        self.drop_sentinel = opt.drop_sentinel
        self.att_hid_size = opt.att_hid_size

        # sentinel embed
        self.sentinel_linear = nn.Sequential(
            nn.Linear(self.rnn_size, self.input_encoding_size),
            nn.ReLU(),
            nn.Dropout(self.drop_sentinel))
        self.sentinel_embed = nn.Linear(self.input_encoding_size, self.att_hid_size)

        # h out embed
        self.ho_linear = nn.Sequential(
            nn.Linear(self.rnn_size, self.input_encoding_size),
            nn.Tanh(),
            nn.Dropout(self.drop_prob_lm))
        self.ho_embed = nn.Linear(self.input_encoding_size, self.att_hid_size)

        self.alpha_net = nn.Linear(self.att_hid_size, 1)
        self.att2h = nn.Linear(self.rnn_size, self.rnn_size)

    def forward(self, top_h, sentinel, conv_feat, conv_feat_embed):
        # conv_feat : att_feats
        # conv_feat_embed : p_att_feats
        # View into three dimensions
        num_regions = conv_feat.size(1)
        # print('num_regions:', num_regions)
        # conv_feat = conv_feat.view(-1, num_regions, self.rnn_size)
        # conv_feat_embed = conv_feat_embed.view(-1, num_regions, self.att_hid_size)
        # print('Conv_feat and conv_feat_embed shapes:', conv_feat.size(), conv_feat_embed.size())
        sentinel = self.sentinel_linear(sentinel)
        sentinel_embed = self.sentinel_embed(sentinel)
        h_out_linear = self.ho_linear(top_h)
        h_out_embed = self.ho_embed(h_out_linear)
        txt_replicate = h_out_embed.unsqueeze(1).expand(h_out_embed.size(0), num_regions + 1, h_out_embed.size(1))
        # img_all = torch.cat([sentinel.view(-1,1,self.input_encoding_size), conv_feat], 1)
        img_all = torch.cat([sentinel.unsqueeze(1), conv_feat], 1)
        # img_all_embed = torch.cat([sentinel_embed.view(-1,1,self.input_encoding_size), conv_feat_embed], 1)
        img_all_embed = torch.cat([sentinel_embed.unsqueeze(1), conv_feat_embed], 1)
        hA = F.tanh(img_all_embed + txt_replicate)
        hA = F.dropout(hA,self.drop_prob_lm, self.training)
        hAflat = self.alpha_net(hA.view(-1, self.att_hid_size))
        PI = F.softmax(hAflat.view(-1, num_regions + 1))
        # self.logger.warn('betas: %s', str(PI.data[:, 0].squeeze(0).cpu().numpy()))
        visAtt = torch.bmm(PI.unsqueeze(1), img_all)
        visAttdim = visAtt.squeeze(1)
        atten_out = visAttdim + h_out_linear
        h = F.tanh(self.att2h(atten_out))
        h = F.dropout(h, self.drop_prob_lm, self.training)
        return h


class Attention(nn.Module):
    def __init__(self, opt):
        super(Attention, self).__init__()
        self.rnn_size = opt.rnn_size
        self.att_hid_size = opt.att_hid_size
        self.h2att = nn.Linear(self.rnn_size, self.att_hid_size)
        self.alpha_net = nn.Linear(self.att_hid_size, 1)

    def forward(self, h, att_feats, p_att_feats):
        # The p_att_feats here is already projected
        att_size = att_feats.numel() // att_feats.size(0) // self.rnn_size
        att = p_att_feats.view(-1, att_size, self.att_hid_size)

        att_h = self.h2att(h)                        # batch * att_hid_size
        att_h = att_h.unsqueeze(1).expand_as(att)            # batch * att_size * att_hid_size
        dot = att + att_h                                   # batch * att_size * att_hid_size
        dot = F.tanh(dot)                                # batch * att_size * att_hid_size
        dot = dot.view(-1, self.att_hid_size)               # (batch * att_size) * att_hid_size
        dot = self.alpha_net(dot)                           # (batch * att_size) * 1
        dot = dot.view(-1, att_size)                        # batch * att_size

        weight = F.softmax(dot)                             # batch * att_size
        att_feats_ = att_feats.view(-1, att_size, self.rnn_size) # batch * att_size * att_feat_size
        att_res = torch.bmm(weight.unsqueeze(1), att_feats_).squeeze(1) # batch * att_feat_size

        return att_res, weight



