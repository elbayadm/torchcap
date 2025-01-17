"""
Define a language model
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import *
import misc.utils as utils
from misc.cvae import VAE

class MultiVAE_LM_encoder(nn.Module):
    def __init__(self, opt):
        super(MultiVAE_LM_encoder, self).__init__()
        self.vocab_size = opt.vocab_size
        self.input_encoding_size = opt.input_encoding_size
        self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size - opt.z_size
        self.z_size = opt.z_size
        self.z_interm_size = opt.z_interm_size
        self.num_layers = opt.num_layers
        self.drop_prob_lm = opt.drop_prob_lm
        self.seq_length = opt.seq_length
        self.num_related = opt.seq_per_img # or a separate param
        self.core = getattr(nn, self.rnn_type.upper())(self.input_encoding_size, self.rnn_size, self.num_layers, bias=False, dropout=self.drop_prob_lm)
        self.embed = nn.Embedding(self.vocab_size + 1, self.input_encoding_size)  # max_norm=1.0)
        self.drop_x_lm = nn.Dropout(p=opt.drop_x_lm)
        #VAE block:
        self.vae = VAE(input_dim=self.rnn_size,
                       latent_dim=self.z_size,
                       h_dim=self.z_interm_size)
        self.init_weights()
        opt.logger.warn('Language Model (vae encoder) : %s' % str(self._modules))

    def init_weights(self):
        initrange = 0.1
        self.embed.weight.data.uniform_(-initrange, initrange)
        self.vae.init_weights()

    def init_hidden(self, bsz):
        weight = next(self.parameters()).data
        if self.rnn_type == 'lstm':
            return (Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()),
                    Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()))
        else:
            return Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_())

    def forward(self, seq):
        # seq (batchsize, sequence length, token index)
        # remove bos and eos:

        batch_size = seq.size(0)
        state = self.init_hidden(batch_size)
        for i in range(1, seq.size(1)):
            it = seq[:, i].clone()
            if it.data.sum():
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)
                output, state = self.core(xt.unsqueeze(0), state)
            else:
                break
        rnn_state = output.squeeze(0)
        num_groups = rnn_state.size(0) // self.num_related
        rnn_per_group = rnn_state.chunk(num_groups)
        rnn_mean = torch.cat([torch.mean(t, dim=0).repeat(self.num_related, 1) for t in rnn_per_group], dim=0)
        #  print rnn_mean, rnn_state
        # Encode via VAE:
        z_mu, z_var , z = self.vae(rnn_state)
        return z_mu, z_var, torch.cat([rnn_mean, z], 1)

    def sample_group(self, seq):
        # seq (batchsize, sequence length, token index)
        # remove bos and eos:

        batch_size = seq.size(0)
        state = self.init_hidden(batch_size)
        for i in range(1, seq.size(1)):
            it = seq[:, i].clone()
            if it.data.sum():
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)
                output, state = self.core(xt.unsqueeze(0), state)
            else:
                break
        rnn_state = output.squeeze(0)
        num_groups = rnn_state.size(0) // self.num_related
        rnn_per_group = rnn_state.chunk(num_groups)
        rnn_mean = torch.cat([torch.mean(t, dim=0).repeat(self.num_related, 1) for t in rnn_per_group], dim=0)
        #  print rnn_mean, rnn_state
        # Encode via VAE:
        #  z_mu, z_var , z = self.vae(rnn_state)
        #  z = Variable(torch.randn(batch_size, self.z_size)).cuda()
        z = Variable(torch.mul(torch.randn(batch_size, self.z_size), 10)).cuda()
        #  print z

        return torch.cat([rnn_mean, z], 1)

    def sample(self, seq):
        # seq (batchsize, sequence length, token index)
        # remove bos and eos:

        batch_size = seq.size(0)
        state = self.init_hidden(batch_size)
        for i in range(1, seq.size(1)):
            it = seq[:, i].clone()
            if it.data.sum():
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)
                output, state = self.core(xt.unsqueeze(0), state)
            else:
                break
        rnn_state = output.squeeze(0)
        # Encode via VAE:
        z = Variable(torch.mul(torch.randn(batch_size, self.z_size), 10)).cuda()
        return torch.cat([rnn_state, z], 1)


class VAE_LM_encoder(nn.Module):
    def __init__(self, opt):
        super(VAE_LM_encoder, self).__init__()
        self.vocab_size = opt.vocab_size
        self.input_encoding_size = opt.input_encoding_size
        self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size - opt.z_size
        self.z_size = opt.z_size
        self.z_interm_size = opt.z_interm_size
        self.num_layers = opt.num_layers
        self.drop_prob_lm = opt.drop_prob_lm
        self.seq_length = opt.seq_length
        self.core = getattr(nn, self.rnn_type.upper())(self.input_encoding_size, self.rnn_size, self.num_layers, bias=False, dropout=self.drop_prob_lm)
        self.embed = nn.Embedding(self.vocab_size + 1, self.input_encoding_size)  # max_norm=1.0)
        self.drop_x_lm = nn.Dropout(p=opt.drop_x_lm)
        #VAE block:
        self.vae = VAE(input_dim=self.rnn_size,
                       latent_dim=self.z_size,
                       h_dim=self.z_interm_size)
        self.init_weights()
        opt.logger.warn('Language Model (vae encoder) : %s' % str(self._modules))

    def init_weights(self):
        initrange = 0.1
        self.embed.weight.data.uniform_(-initrange, initrange)
        self.vae.init_weights()

    def init_hidden(self, bsz):
        weight = next(self.parameters()).data
        if self.rnn_type == 'lstm':
            return (Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()),
                    Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()))
        else:
            return Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_())

    def forward(self, seq):
        # seq (batchsize, sequence length, token index)
        # remove bos and eos:

        batch_size = seq.size(0)
        state = self.init_hidden(batch_size)
        for i in range(1, seq.size(1)):
            it = seq[:, i].clone()
            if it.data.sum():
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)
                output, state = self.core(xt.unsqueeze(0), state)
            else:
                break
        rnn_state = output.squeeze(0)
        # Encode via VAE:
        z_mu, z_var , z = self.vae(rnn_state)
        return z_mu, z_var, torch.cat([rnn_state, z], 1)

    def sample(self, seq):
        # seq (batchsize, sequence length, token index)
        # remove bos and eos:

        batch_size = seq.size(0)
        state = self.init_hidden(batch_size)
        for i in range(1, seq.size(1)):
            it = seq[:, i].clone()
            if it.data.sum():
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)
                output, state = self.core(xt.unsqueeze(0), state)
            else:
                break
        rnn_state = output.squeeze(0)
        # Encode via VAE:
        z = Variable(torch.randn(batch_size, self.z_size)).cuda()
        return torch.cat([rnn_state, z], 1)



class LM_encoder(nn.Module):
    def __init__(self, opt):
        super(LM_encoder, self).__init__()
        self.vocab_size = opt.vocab_size
        self.input_encoding_size = opt.input_encoding_size
        self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size
        self.num_layers = opt.num_layers
        self.drop_prob_lm = opt.drop_prob_lm
        self.seq_length = opt.seq_length
        self.core = getattr(nn, self.rnn_type.upper())(self.input_encoding_size, self.rnn_size, self.num_layers, bias=False, dropout=self.drop_prob_lm)
        self.embed = nn.Embedding(self.vocab_size + 1, self.input_encoding_size)  # max_norm=1.0)
        self.drop_x_lm = nn.Dropout(p=opt.drop_x_lm)
        self.init_weights()
        opt.logger.warn('Language Model (encoder) : %s' % str(self._modules))

    def init_weights(self):
        initrange = 0.1
        self.embed.weight.data.uniform_(-initrange, initrange)

    def init_hidden(self, bsz):
        weight = next(self.parameters()).data
        if self.rnn_type == 'lstm':
            return (Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()),
                    Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()))
        else:
            return Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_())

    def forward(self, seq):
        # seq (batchsize, sequence length, token index)
        # remove bos and eos:

        batch_size = seq.size(0)
        state = self.init_hidden(batch_size)
        for i in range(1, seq.size(1)):
            it = seq[:, i].clone()
            if it.data.sum():
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)
                output, state = self.core(xt.unsqueeze(0), state)
            else:
                break
        return output.squeeze(0)


class LM_decoder(nn.Module):
    def __init__(self, opt):
        super(LM_decoder, self).__init__()
        self.vocab_size = opt.vocab_size
        self.input_encoding_size = opt.input_encoding_size
        self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size
        self.num_layers = opt.num_layers
        self.drop_prob_lm = opt.drop_prob_lm
        self.seq_length = opt.seq_length
        self.text_code_size = opt.rnn_size
        self.ss_prob = 0.0 # Schedule sampling probability
        self.text_code_embed = nn.Linear(self.text_code_size, self.input_encoding_size)
        self.core = getattr(nn, self.rnn_type.upper())(self.input_encoding_size, self.rnn_size, self.num_layers, bias=False, dropout=self.drop_prob_lm)
        self.embed = nn.Embedding(self.vocab_size + 1, self.input_encoding_size)  # max_norm=1.0)
        self.drop_x_lm = nn.Dropout(p=opt.drop_x_lm)
        self.logit = nn.Linear(self.rnn_size, self.vocab_size + 1)
        self.init_weights()
        opt.logger.warn('Language Model (decoder) : %s' % str(self._modules))

    def init_weights(self):
        initrange = 0.1
        self.embed.weight.data.uniform_(-initrange, initrange)
        self.text_code_embed.weight.data.uniform_(-initrange, initrange)
        self.text_code_embed.bias.data.fill_(0)
        self.logit.bias.data.fill_(0)
        self.logit.weight.data.uniform_(-initrange, initrange)

    def init_hidden(self, bsz):
        weight = next(self.parameters()).data
        if self.rnn_type == 'lstm':
            return (Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()),
                    Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_()))
        else:
            return Variable(weight.new(self.num_layers, bsz, self.rnn_size).zero_())

    def forward(self, text_code, seq):
        batch_size = text_code.size(0)
        state = self.init_hidden(batch_size)
        outputs = []

        for i in range(seq.size(1)):
            if i == 0:
                xt = self.text_code_embed(text_code)
            else:
                if i >= 2 and self.ss_prob > 0.0: # otherwiste no need to sample
                    sample_prob = text_code.data.new(batch_size).uniform_(0, 1)
                    sample_mask = sample_prob < self.ss_prob
                    if sample_mask.sum() == 0:
                        it = seq[:, i-1].clone()
                    else:
                        sample_ind = sample_mask.nonzero().view(-1)
                        it = seq[:, i-1].data.clone()
                        #prob_prev = torch.exp(outputs[-1].data.index_select(0, sample_ind)) # fetch prev distribution: shape Nx(M+1)
                        #it.index_copy_(0, sample_ind, torch.multinomial(prob_prev, 1).view(-1))
                        prob_prev = torch.exp(outputs[-1].data) # fetch prev distribution: shape Nx(M+1)
                        it.index_copy_(0, sample_ind, torch.multinomial(prob_prev, 1).view(-1).index_select(0, sample_ind))
                        it = Variable(it, requires_grad=False)
                else:
                    it = seq[:, i-1].clone()
                # break if all the sequences end
                if i >= 2 and seq[:, i-1].data.sum() == 0:
                    break
                xt = self.embed(it)
                xt = self.drop_x_lm(xt)

            output, state = self.core(xt.unsqueeze(0), state)
            output = F.log_softmax(self.logit(output.squeeze(0)))
            outputs.append(output)

        return torch.cat([_.unsqueeze(1) for _ in outputs[1:]], 1).contiguous()

    def sample_beam(self, text_code, opt={}):
        beam_size = opt.get('beam_size', 10)
        batch_size = text_code.size(0)

        assert beam_size <= self.vocab_size + 1, 'lets assume this for now, otherwise this corner case causes a few headaches down the road. can be dealt with in future if needed'
        seq = torch.LongTensor(self.seq_length, batch_size).zero_()
        seqLogprobs = torch.FloatTensor(self.seq_length, batch_size)
        # lets process every image independently for now, for simplicity

        self.done_beams = [[] for _ in range(batch_size)]
        for k in range(batch_size):
            state = self.init_hidden(beam_size)

            beam_seq = torch.LongTensor(self.seq_length, beam_size).zero_()
            beam_seq_logprobs = torch.FloatTensor(self.seq_length, beam_size).zero_()
            beam_logprobs_sum = torch.zeros(beam_size) # running sum of logprobs for each beam
            for t in range(self.seq_length + 2):
                if t == 0:
                    xt = self.text_code_embed(text_code[k:k+1]).expand(beam_size, self.input_encoding_size)
                elif t == 1: # input <bos>
                    it = text_code.data.new(beam_size).long().zero_()
                    xt = self.embed(Variable(it, requires_grad=False))
                else:
                    """perform a beam merge. that is,
                    for every previous beam we now many new possibilities to branch out
                    we need to resort our beams to maintain the loop invariant of keeping
                    the top beam_size most likely sequences."""
                    logprobsf = logprobs.float() # lets go to CPU for more efficiency in indexing operations
                    ys,ix = torch.sort(logprobsf,1,True) # sorted array of logprobs along each previous beam (last true = descending)
                    candidates = []
                    cols = min(beam_size, ys.size(1))
                    rows = beam_size
                    if t == 2:  # at first time step only the first beam is active
                        rows = 1
                    for c in range(cols):
                        for q in range(rows):
                            # compute logprob of expanding beam q with word in (sorted) position c
                            local_logprob = ys[q,c]
                            candidate_logprob = beam_logprobs_sum[q] + local_logprob
                            candidates.append({'c':ix.data[q,c], 'q':q, 'p':candidate_logprob.data[0], 'r':local_logprob.data[0]})
                    candidates = sorted(candidates, key=lambda x: -x['p'])

                    # construct new beams
                    new_state = [_.clone() for _ in state]
                    if t > 2:
                        # well need these as reference when we fork beams around
                        beam_seq_prev = beam_seq[:t-2].clone()
                        beam_seq_logprobs_prev = beam_seq_logprobs[:t-2].clone()
                    for vix in range(beam_size):
                        v = candidates[vix]
                        # fork beam index q into index vix
                        if t > 2:
                            beam_seq[:t-2, vix] = beam_seq_prev[:, v['q']]
                            beam_seq_logprobs[:t-2, vix] = beam_seq_logprobs_prev[:, v['q']]

                        # rearrange recurrent states
                        for state_ix in range(len(new_state)):
                            # copy over state in previous beam q to new beam at vix
                            new_state[state_ix][0, vix] = state[state_ix][0, v['q']] # dimension one is time step

                        # append new end terminal at the end of this beam
                        beam_seq[t-2, vix] = v['c'] # c'th word is the continuation
                        beam_seq_logprobs[t-2, vix] = v['r'] # the raw logprob here
                        beam_logprobs_sum[vix] = v['p'] # the new (sum) logprob along this beam

                        if v['c'] == 0 or t == self.seq_length + 1:
                            # END token special case here, or we reached the end.
                            # add the beam to a set of done beams
                            self.done_beams[k].append({'seq': beam_seq[:, vix].clone(),
                                                'logps': beam_seq_logprobs[:, vix].clone(),
                                                'p': beam_logprobs_sum[vix]
                                                })
                    # encode as vectors
                    it = beam_seq[t-2]
                    xt = self.embed(Variable(it.cuda()))

                if t >= 2:
                    state = new_state

                output, state = self.core(xt.unsqueeze(0), state)
                logprobs = F.log_softmax(self.logit(output.squeeze(0)))

            self.done_beams[k] = sorted(self.done_beams[k], key=lambda x: -x['p'])
            seq[:, k] = self.done_beams[k][0]['seq'] # the first beam has highest cumulative score
            seqLogprobs[:, k] = self.done_beams[k][0]['logps']
        # return the samples and their log likelihoods
        return seq.transpose(0, 1), seqLogprobs.transpose(0, 1)

    def sample_ltd(self, text_code, indices, opt={}):
        """
        Sample limited to a vocab
        """
        sample_max = opt.get('sample_max', 1)
        beam_size = opt.get('beam_size', 1)
        temperature = opt.get('temperature', 1.0)
        forbid_unk = opt.get('forbid_unk', 1)
        unk_index = opt.get('vocab_size')

        batch_size = text_code.size(0)
        state = self.init_hidden(batch_size)
        seq = []
        seqLogprobs = []
        for t in range(self.seq_length + 2):
            if t == 0:
                xt = self.text_code_embed(text_code)
            else:
                if t == 1: # input <bos>
                    it = text_code.data.new(batch_size).long().zero_()
                elif sample_max:
                    sampleLogprobs, it = torch.max(logprobs.data, 1)
                    it = it.view(-1).long()
                else:
                    if temperature == 1.0:
                        prob_prev = torch.exp(logprobs.data).cpu() # fetch prev distribution: shape Nx(M+1)
                    else:
                        # scale logprobs by temperature
                        prob_prev = torch.exp(torch.div(logprobs.data, temperature)).cpu()
                    it = torch.multinomial(prob_prev, 1).cuda()
                    sampleLogprobs = logprobs.gather(1, Variable(it, requires_grad=False)) # gather the logprobs at sampled positions
                    it = it.view(-1).long() # and flatten indices for downstream processing

                xt = self.embed(Variable(it, requires_grad=False))

            if t >= 2:
                # stop when all finished
                if t == 2:
                    unfinished = it > 0
                else:
                    unfinished = unfinished * (it > 0)
                if unfinished.sum() == 0:
                    break
                it = it * unfinished.type_as(it)
                seq.append(it) #seq[t] the input of t+2 time step
                seqLogprobs.append(sampleLogprobs.view(-1))

            output, state = self.core(xt.unsqueeze(0), state)
            logprobs = F.log_softmax(self.logit(output.squeeze(0)))
            #  print "logprobs:", logprobs.data[:, :20]
            for token in indices:
                logprobs[:, token] += 5
            if forbid_unk:
                logpros = logprobs[:, :-1]
                #  print "logprobs post:", logprobs.data[:, :20]
        return torch.cat([_.unsqueeze(1) for _ in seq], 1), torch.cat([_.unsqueeze(1) for _ in seqLogprobs], 1)




    def sample(self, text_code, opt={}):
        sample_max = opt.get('sample_max', 1)
        beam_size = opt.get('beam_size', 1)
        temperature = opt.get('temperature', 1.0)
        forbid_unk = opt.get('forbid_unk', 1)
        unk_index = opt.get('vocab_size')

        if beam_size > 1:
            return self.sample_beam(text_code, opt)

        batch_size = text_code.size(0)
        state = self.init_hidden(batch_size)
        seq = []
        seqLogprobs = []
        for t in range(self.seq_length + 2):
            if t == 0:
                xt = self.text_code_embed(text_code)
            else:
                if t == 1: # input <bos>
                    it = text_code.data.new(batch_size).long().zero_()
                elif sample_max:
                    sampleLogprobs, it = torch.max(logprobs.data, 1)
                    it = it.view(-1).long()
                else:
                    if temperature == 1.0:
                        prob_prev = torch.exp(logprobs.data).cpu() # fetch prev distribution: shape Nx(M+1)
                    else:
                        # scale logprobs by temperature
                        prob_prev = torch.exp(torch.div(logprobs.data, temperature)).cpu()
                    it = torch.multinomial(prob_prev, 1).cuda()
                    sampleLogprobs = logprobs.gather(1, Variable(it, requires_grad=False)) # gather the logprobs at sampled positions
                    it = it.view(-1).long() # and flatten indices for downstream processing

                xt = self.embed(Variable(it, requires_grad=False))

            if t >= 2:
                # stop when all finished
                if t == 2:
                    unfinished = it > 0
                else:
                    unfinished = unfinished * (it > 0)
                if unfinished.sum() == 0:
                    break
                it = it * unfinished.type_as(it)
                seq.append(it) #seq[t] the input of t+2 time step
                seqLogprobs.append(sampleLogprobs.view(-1))

            output, state = self.core(xt.unsqueeze(0), state)
            logprobs = F.log_softmax(self.logit(output.squeeze(0)))
            if forbid_unk:
                logprobs = logprobs[:, :-1]


        return torch.cat([_.unsqueeze(1) for _ in seq], 1), torch.cat([_.unsqueeze(1) for _ in seqLogprobs], 1)
