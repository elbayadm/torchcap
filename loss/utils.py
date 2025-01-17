import math
import numpy as np
import torch
from torch.autograd import Variable


def to_contiguous(tensor):
    """
    Convert tensor if not contiguous
    """
    if tensor.is_contiguous():
        return tensor
    else:
        return tensor.contiguous()


def decode_sequence(ix_to_word, seq):
    """
    Decode sequence into natural language
    Input: seq, N*D numpy array, with element 0 .. vocab_size. 0 is END token.
    """
    N, D = seq.size()
    out = []
    for i in range(N):
        txt = ''
        for j in range(D):
            ix = seq[i, j].item()
            if ix > 0:
                if j >= 1:
                    txt = txt + ' '
                txt = txt + ix_to_word[str(ix)]
            else:
                break
        out.append(txt)
    return out


def rows_entropy(distrib):
    """
    return the entropy of each row in the given distributions
    """
    return torch.sum(distrib * torch.log(distrib), dim=1)


def get_indices_vocab(target, seq_per_img):
    seq_length = target.size(1)
    num_img = target.size(0) // seq_per_img
    vocab_per_image = target.chunk(num_img)
    vocab_per_image = [np.unique(to_contiguous(t).data.cpu().numpy())
                       for t in vocab_per_image]
    max_vocab = max([len(t) for t in vocab_per_image])
    vocab_per_image = [np.pad(t, (0, max_vocab - len(t)), 'constant')
                       for t in vocab_per_image]
    indices_vocab = Variable(torch.cat([torch.from_numpy(t).\
                             repeat(seq_per_img * seq_length, 1)
                             for t in vocab_per_image], dim=0)).cuda()
    return indices_vocab


def get_ml_loss(logp, target, mask, scores=None, norm=True, penalize=0):
    """
    Compute the usual ML loss
    """
    seq_length = logp.size(1)
    target = target[:, :seq_length]
    mask = mask[:, :seq_length]
    binary_mask = mask
    if scores is not None:
        # row_scores = scores.unsqueeze(1).repeat(1, seq_length)
        row_scores = scores.repeat(1, seq_length)
        mask = torch.mul(mask, row_scores)
    logp = to_contiguous(logp).view(-1, logp.size(2))
    target = to_contiguous(target).view(-1, 1)
    mask = to_contiguous(mask).view(-1, 1)
    if penalize:
        logp = logp.gather(1, target)
        neg_entropy = torch.sum(torch.exp(logp) * logp)
        ml_output = torch.sum(-logp * mask) + penalize * neg_entropy
    else:
        ml_output = - logp.gather(1, target) * mask
        ml_output = torch.sum(ml_output)
    if norm:
        ml_output /= torch.sum(binary_mask)
    return ml_output


