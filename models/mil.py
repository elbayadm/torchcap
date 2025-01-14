import numpy as np
import torch
import torch.nn as nn
import os
from torch.autograd import Variable
from torch.utils.serialization import load_lua
import torch.nn.functional as F
import cv2
import torch.utils.model_zoo as model_zoo
from .cnn import model_urls, model_configs, L2Norm

def upsample_images(IMB, sz):
    """
    Upsample images of generated batch:
        input: (N, C, W, H)
        sz : desired size
    """
    N, C, w, h = IMB.shape
    s = np.float(max(h, w))
    OUT = np.zeros((N, C, sz, sz))
    for index in range(N):
        im = IMB[index].transpose(2, 1, 0)
        I = cv2.resize(im, None, None, fx=np.float(sz) / s, fy=np.float(sz) / s,
                       interpolation=cv2.INTER_LINEAR)
        I_out = np.zeros((sz, sz, 3), dtype=np.float)
        I_out[0:I.shape[0], 0:I.shape[1], :] = I
        I_out = I_out.transpose(2, 1, 0)
        OUT[index] = I_out
    return OUT


def upsample_image(im, sz):
    h = im.shape[0]
    w = im.shape[1]
    s = np.float(max(h, w))
    I_out = np.zeros((sz, sz, 3), dtype=np.float);
    I = cv2.resize(im, None, None, fx=np.float(sz) / s, fy=np.float(sz) / s, interpolation=cv2.INTER_LINEAR);
    SZ = I.shape;
    I_out[0:I.shape[0], 0:I.shape[1], :] = I;
    return I_out, I, SZ




class MIL_crit(nn.Module):
    def __init__(self, opt):
        super(MIL_crit, self).__init__()
        self.opt = opt
        self.seq_per_img = opt.seq_per_img

    def forward(self, input, target):
        """
        input: prob(w\in Image): shape: #images, #vocab
        target: labels         : shape: #images * #seq_per_img, #seq_length
        Beware batch_size = 1
        """
        # input = torch.log(input + 1e-30)
        # print("Probs:", input)
        # parse words in image from labels:
        num_img = input.size(0)
        # assert num_img == 1, "Batch size larger than 1"
        words_per_image = np.unique(to_contiguous(target).data.cpu().numpy())
        # print('Word in image:', words_per_image)
        indices_pos = Variable(torch.from_numpy(words_per_image).view(1, -1), requires_grad=False).cuda()
        indices_neg = Variable(torch.from_numpy(np.array([a for a in np.arange(self.opt.vocab_size) if a not in words_per_image])).view(1, -1), requires_grad=False).cuda()
        mask_pos = torch.gt(indices_pos, 0).float()
        mask_neg = torch.gt(indices_neg, 0).float()
        # print('Positives:', torch.sum(mask_pos), "Negatives:", torch.sum(mask_neg))
        log_pos = - torch.sum(torch.log(input + 1e-30).gather(1, indices_pos) * mask_pos)
        log_neg = - torch.sum(torch.log(1 - input + 1e-15).gather(1, indices_neg) * mask_neg)
        # print('Log_pos:', log_pos, 'log_neg:', log_neg)
        out = log_pos / torch.sum(mask_pos) + log_neg / torch.sum(mask_neg)
        # print("Final output:", out)
        return out


class ResNet_MIL_corr(nn.Module):
    """
    Wrapper for ResNet with MIL
    """
    def __init__(self, opt):
        self.opt = opt
        super(ResNet_MIL_corr, self).__init__()
        self.resnet = ResNetModel(opt)
        #  self.pool_mil = nn.MaxPool2d(kernel_size=7, stride=0)
        self.classifier = nn.Linear(2048, opt.vocab_size)
        self.sigmoid = nn.Sigmoid()
        self.softmax = nn.Softmax()
        #  print "Modules:", self._modules

    def init_added_weights(self):
        initrange = 0.1
        self.classifier.bias.data.fill_(0)
        self.classifier.weight.data.uniform_(-initrange, initrange)

    def forward(self, x):
        x0, _ = self.resnet(x)
        x0 = to_contiguous(x0.permute(0, 2, 3, 1))
        x = x0.view(x0.size(0) * x0.size(1) * x0.size(2), -1)
        x = self.classifier(x)
        x = self.softmax(self.sigmoid(x))
        x = x.view(x0.size(0), x0.size(1) * x0.size(2), -1)
        probs =  torch.log(1 - torch.prod(1 - x, dim=1))
        self.opt.logger.error('Final probs: %s' % str(probs))
        probs = probs.squeeze(1)
        return probs



class ResNet_MIL(nn.Module):
    """
    Wrapper for ResNet with MIL
    """
    def __init__(self, opt):
        self.opt = opt
        super(ResNet_MIL, self).__init__()
        self.resnet = ResNetModel(opt)
        #  self.sigmoid = torch.nn.Sigmoid()
        #  self.pool_mil = nn.MaxPool2d(kernel_size=7, stride=0)
        self.classifier = nn.Linear(49, opt.vocab_size)
        #  print "Modules:", self._modules

    def init_added_weights(self):
        initrange = 1.0
        self.classifier.bias.data.fill_(0)
        self.classifier.weight.data.uniform_(-initrange, initrange)

    def forward(self, x):
        x0, _ = self.resnet(x)
        #  print "Resnet output:", x0.size()
        #  x = self.pool_mil(x0)
        x = x0.view(x0.size(0) * x0.size(1), -1)
        #  x = x0.resize(x0.size(0) * x0.size(1), -1)
        #  print 'Mil output:', x.size()
        #  x = x.squeeze(2).squeeze(2)
        x = self.classifier(x)
        #  print "Classified:", x.size()
        #  x = self.sigmoid(x)
        x = F.log_softmax(x)
        x = x.view(x0.size(0), x0.size(1), -1)
        #  print "Resized:", x.size()
        probs, cands = torch.max(x, 1)
        probs = probs.squeeze(1)
        #  print "vocab probs:", probs.size()
        return probs


class VGG_MIL(nn.Module):
    def __init__(self, opt):
        super(VGG_MIL, self).__init__()
        self.opt = opt
        self.num_words = opt.vocab_size - 1
        self.start_from = opt.start_from
        self.cnn_weight = opt.cnn_weight

        self.conv = torch.nn.Sequential()
        self.conv.add_module("conv1_1", nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_1_1", torch.nn.ReLU())
        self.conv.add_module("conv1_2", nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_1_2", torch.nn.ReLU())
        self.conv.add_module("maxpool_1", torch.nn.MaxPool2d(kernel_size=2))

        self.conv.add_module("conv2_1", nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_2_1", torch.nn.ReLU())
        self.conv.add_module("conv2_2", nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_2_2", torch.nn.ReLU())
        self.conv.add_module("maxpool_2", torch.nn.MaxPool2d(kernel_size=2))

        self.conv.add_module("conv3_1", nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_3_1", torch.nn.ReLU())
        self.conv.add_module("conv3_2", nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_3_2", torch.nn.ReLU())
        self.conv.add_module("conv3_3", nn.Conv2d(256, 256, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_3_3", torch.nn.ReLU())
        self.conv.add_module("maxpool_3", torch.nn.MaxPool2d(kernel_size=2))

        self.conv.add_module("conv4_1", nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_4_1", torch.nn.ReLU())
        self.conv.add_module("conv4_2", nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_4_2", torch.nn.ReLU())
        self.conv.add_module("conv4_3", nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_4_3", torch.nn.ReLU())
        self.conv.add_module("maxpool_4", torch.nn.MaxPool2d(kernel_size=2))

        self.conv.add_module("conv5_1", nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_5_1", torch.nn.ReLU())
        self.conv.add_module("conv5_2", nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_5_2", torch.nn.ReLU())
        self.conv.add_module("conv5_3", nn.Conv2d(512, 512, kernel_size=3, stride=1, padding=1))
        self.conv.add_module("relu_5_3", torch.nn.ReLU())
        self.conv.add_module("maxpool_5", torch.nn.MaxPool2d(kernel_size=2))

        self.fc_conv = torch.nn.Sequential()

        self.fc_conv.add_module("fc_words", nn.Linear(512, self.num_words))
        self.sigmoid = nn.Sigmoid()
        # self.fc_conv.add_module("fc6_conv", nn.Conv2d(512, 4096, kernel_size=7, stride=1, padding=0))
        # self.fc_conv.add_module("relu_6_1", torch.nn.ReLU())

        # self.fc_conv.add_module("fc7_conv", nn.Conv2d(4096, 4096, kernel_size=1, stride=1, padding=0))
        # self.fc_conv.add_module("relu_7_1", torch.nn.ReLU())

        # self.fc_conv.add_module("fc8_conv", nn.Conv2d(4096, self.num_words, kernel_size=1, stride=1, padding=0))
        # self.pool_mil = nn.MaxPool2d(kernel_size=3, stride=0)

        if self.start_from is not None and len(self.cnn_weight) != 0:
            self.load_state_dict(torch.load(self.cnn_weight))
            print("Load pretrained CNN model from " + self.cnn_weight)
        elif self.start_from is not None:
            print("Load pretrained CNN model (from start folder) : " + self.start_from)
            self.load_state_dict(torch.load(os.path.join(self.start_from, 'model-cnn.pth')))
        else:
            print('Loading model from zoo')
            params = model_zoo.load_url(model_urls['vgg16'])
            print(params.keys())
            # Remapping the params:
            params['conv1_1.weight'] = params['features.0.weight']
            del params['features.0.weight']
            params['conv1_1.bias'] = params['features.0.bias']
            del params['features.0.bias']

            params['conv1_2.bias'] = params['features.2.bias']
            del params['features.2.bias']
            params['conv1_2.weight'] = params['features.2.weight']
            del params['features.2.weight']

            params['conv2_1.bias'] = params['features.5.bias']
            del params['features.5.bias']
            params['conv2_1.weight'] = params['features.5.weight']
            del params['features.5.weight']

            params['conv2_2.bias'] = params['features.7.bias']
            del params['features.7.bias']
            params['conv2_2.weight'] = params['features.7.weight']
            del params['features.7.weight']

            params['conv3_1.bias'] = params['features.10.bias']
            del params['features.10.bias']
            params['conv3_1.weight'] = params['features.10.weight']
            del params['features.10.weight']

            params['conv3_2.bias'] = params['features.12.bias']
            del params['features.12.bias']
            params['conv3_2.weight'] = params['features.12.weight']
            del params['features.12.weight']

            params['conv3_3.bias'] = params['features.14.bias']
            del params['features.14.bias']
            params['conv3_3.weight'] = params['features.14.weight']
            del params['features.14.weight']

            params['conv4_1.bias'] = params['features.17.bias']
            del params['features.17.bias']
            params['conv4_1.weight'] = params['features.17.weight']
            del params['features.17.weight']

            params['conv4_2.bias'] = params['features.19.bias']
            del params['features.19.bias']
            params['conv4_2.weight'] = params['features.19.weight']
            del params['features.19.weight']

            params['conv4_3.bias'] = params['features.21.bias']
            del params['features.21.bias']
            params['conv4_3.weight'] = params['features.21.weight']
            del params['features.21.weight']

            params['conv5_1.bias'] = params['features.24.bias']
            del params['features.24.bias']
            params['conv5_1.weight'] = params['features.24.weight']
            del params['features.24.weight']

            params['conv5_2.bias'] = params['features.26.bias']
            del params['features.26.bias']
            params['conv5_2.weight'] = params['features.26.weight']
            del params['features.26.weight']

            params['conv5_3.bias'] = params['features.28.bias']
            del params['features.28.bias']
            params['conv5_3.weight'] = params['features.28.weight']
            del params['features.28.weight']
            K = list(params.keys())
            for k in K:
                if k.startswith('classifier'):
                    del params[k]

            print(params.keys())
            self.conv.load_state_dict(params)


    def forward_extended(self, x):
        xconv = self.conv.forward(x.float())
        # print('conv output:', xconv.size())
        xconv = xconv.permute(0, 2, 3, 1).contiguous()
        xregions = xconv.view(xconv.size(0), xconv.size(1) * xconv.size(2), xconv.size(3))
        # print('Permuted:', xregions.size())
        # Normalize the embeddings
        # rn = torch.norm(xregions, p=2, dim=1).detach()
        # xnorm = xregions.div(rn.expand_as(xregions))
        xnorm = xregions

        # print('Normalized region features:', xnorm)

        # Max pooling over all regions:
        # xmil, _ = torch.max(xnorm, dim=1)
        # xmil = xmil.squeeze(1)
        # print('pool mil:', xmil)

        # Classifiers:
        xf = self.fc_conv(xnorm.view(-1, 512)).view(xconv.size(0), -1, self.num_words)
        # print('fc_conv', xf)
        xf = torch.exp(xf)
        xf = xf.div(xf.sum(dim=2).expand_as(xf))
        # print('Sigmoid:', xf.sum(dim=2))
        # Eval 1 - p(w in region)
        # x1 = x0.view(x.size(0), self.num_words, -1)
        x1 = torch.add(torch.mul(xf, -1), 1)
        prods = torch.prod(x1, 1).squeeze(1)
        # Eval 1 - p(word not in image) ( = prod over regions (p(word not in region)))
        probs = torch.add(torch.mul(prods, -1), 1)
        #  print('x;', x.size())
        # out = torch.max(x, probs)
        # out = torch.log(out)
        # print('Out:', probs)
        return xnorm, xf, probs


    def forward(self, x):
        xconv = self.conv.forward(x.float())
        # print('conv output:', xconv.size())
        xconv = xconv.permute(0, 2, 3, 1).contiguous()
        xregions = xconv.view(xconv.size(0), xconv.size(1) * xconv.size(2), xconv.size(3))
        # print('Permuted:', xregions.size())
        # Normalize the embeddings
        # rn = torch.norm(xregions, p=2, dim=1).detach()
        # xnorm = xregions.div(rn.expand_as(xregions))
        xnorm = xregions
        # print('Normalized region features:', xnorm.size())

        # Max pooling over all regions:
        # xmil, _ = torch.max(xnorm, dim=1)
        # xmil = xmil.squeeze(1)
        # print('pool mil:', xmil)

        # Classifiers:
        code_dim = xnorm.size(2)
        # self.opt.logger.warn('Code dim: %s', str(code_dim))
        # self.opt.logger.warn('#Regions : %s' % str(xnorm.size()))
        xf = self.fc_conv(xnorm.view(-1, code_dim)).view(xconv.size(0), -1, self.num_words)
        # print('fc_conv', xf)
        xf = torch.exp(xf)
        xf = xf.div(xf.sum(dim=2).expand_as(xf))
        # print('Sigmoid:', xf.sum(dim=2))
        # Eval 1 - p(w in region)
        # x1 = x0.view(x.size(0), self.num_words, -1)
        x1 = torch.add(torch.mul(xf, -1), 1)
        prods = torch.prod(x1, 1).squeeze(1)
        # Eval 1 - p(word not in image) ( = prod over regions (p(word not in region)))
        probs = torch.add(torch.mul(prods, -1), 1)
        #  print('x;', x.size())
        # out = torch.max(x, probs)
        # out = torch.log(out)
        # print('Out:', probs)
        return probs

class MIL_Precision_Score_Mapping(nn.Module):
    def __init__(self):
        super(MIL_Precision_Score_Mapping, self).__init__()
        self.mil = nn.MaxPool2d(kernel_size=11, stride=0)

    def forward(self, x, score, precision, mil_prob):
        out = self.mil(x)
        return out

