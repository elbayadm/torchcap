import os.path as osp
from six.moves import cPickle as pickle
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import misc.loss as loss


class DecoderModel(nn.Module):
    def __init__(self, opt):
        super(DecoderModel, self).__init__()
        self.vocab_size = opt.vocab_size
        self.use_glove = opt.use_glove
        if self.use_glove:
            self.input_encoding_size = 300
        else:
            self.input_encoding_size = opt.input_encoding_size
        self.rnn_type = opt.rnn_type
        self.rnn_size = opt.rnn_size
        self.num_layers = opt.num_layers
        self.drop_prob_lm = opt.drop_prob_lm
        self.seq_length = opt.seq_length
        self.fc_feat_size = opt.fc_feat_size
        self.num_regions = opt.num_regions  # Or the number of candidate regions
        self.att_feat_size = opt.att_feat_size
        self.opt = opt
        self.logger = opt.logger
        self.ss_prob = 0.0 # Schedule sampling probability
        self.ss_vocab = opt.scheduled_sampling_vocab

    def load(self):
        opt = self.opt
        if vars(opt).get('start_from', None) is not None:
            # check if all necessary files exist
            assert osp.isfile(opt.infos_start_from),\
                    "infos file %s does not exist" % opt.start_from
            saved = torch.load(opt.start_from)
            for k in list(saved):
                if 'crit' in k:
                    self.logger.warn('Deleting key %s' % k)
                    del saved[k]
            self.logger.warn('Loading the model dict (last checkpoint) %s'\
                             % str(list(saved.keys())))
            self.load_state_dict(saved)

    def define_loss(self, vocab):
        opt = self.opt
        if opt.sample_cap:
            # Sampling from the captioning model itself
            if 'cider' in opt.loss_version:
                crit = loss.CiderRewardCriterion(opt, vocab)
            elif 'hamming' in opt.loss_version:
                crit = loss.HammingRewardCriterion(opt)
            elif 'infersent' in opt.loss_version:
                crit = loss.InfersentRewardCriterion(opt, vocab)
            elif 'bleu' in opt.loss_version:
                crit = loss.BleuRewardCriterion(opt, vocab)
            elif 'word' in opt.loss_version:
                crit = loss.WordSmoothCriterion(opt)
        elif opt.bootstrap:
            crit = loss.DataAugmentedCriterion(opt)
        elif opt.combine_caps_losses:
            crit = loss.MultiLanguageModelCriterion(opt.seq_per_img)
        else:
            # The defualt ML
            opt.logger.warn('Using baseline loss criterion')
            crit = loss.LanguageModelCriterion(opt)
        self.crit = crit

    def step(self, data, att_feats, fc_feats):
        opt = self.opt
        if opt.bootstrap:
            if opt.bootstrap_score in ["cider", "cider-exp"]:
                tmp = [data['labels'], data['masks'], data['scores'], data['cider']]
                tmp = [Variable(torch.from_numpy(_), requires_grad=False).cuda() for _ in tmp]
                labels, masks, scores, s_scores= tmp

            elif opt.bootstrap_score in ["bleu4", "bleu4-exp"]:
                tmp = [data['labels'], data['masks'], data['scores'], data['bleu']]
                tmp = [Variable(torch.from_numpy(_), requires_grad=False).cuda() for _ in tmp]
                labels, masks, scores, s_scores = tmp

            elif opt.bootstrap_score in ["infersent", "infersent-exp"]:
                tmp = [data['labels'], data['masks'], data['scores'], data['infersent']]
                tmp = [Variable(torch.from_numpy(_), requires_grad=False).cuda() for _ in tmp]
                labels, masks, scores, s_scores = tmp
            else:
                raise ValueError('Unknown bootstrap distribution %s' % opt.bootstrap_score)
            # Exponentiate the scores
            if "exp" in opt.bootstrap_score:
                print('Original rewards:', torch.mean(s_scores))
                s_scores = torch.exp(torch.div(s_scores, opt.raml_tau))
                print('Tempering the reward:', torch.mean(s_scores))
            scores = torch.div(s_scores, torch.exp(scores))
            opt.logger.debug('Mean importance scores: %.3e' % torch.mean(scores).data[0])
        else:
            tmp = [data['labels'], data['masks'], data['scores']]
            tmp = [Variable(torch.from_numpy(_), requires_grad=False).cuda() for _ in tmp]
            labels, masks, scores = tmp

        # if opt.caption_model == "show_tell_vae":
                # preds, recon_loss, kld_loss = self.forward(fc_feats, att_feats, labels)
                # real_loss, loss = self.crit(preds, labels[:, 1:], masks[:, 1:])
                # loss += opt.vae_weight * (recon_loss + opt.kld_weight * kld_loss)
                # #FIXME add the scaling as parameter

        # FIXME Deprecated
        if opt.caption_model == 'show_tell_raml':
            probs, reward = self.forward(fc_feats, att_feats, labels)
            raml_scores = reward * Variable(torch.ones(scores.size()))
            # raml_scores = Variable(torch.ones(scores.size()))
            print('Raml reward:', reward)
            ml_loss, loss = self.crit(probs, labels[:, 1:], masks[:, 1:], raml_scores)
        else:
            ml_loss, loss = self.crit(self.forward(fc_feats, att_feats, labels),
                                        labels[:, 1:], masks[:, 1:], scores)
        return ml_loss, loss


