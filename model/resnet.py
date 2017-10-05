#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

__author__ = 'Liu Lihao'

logger = logging.getLogger()


class Resnet(object):
    def __init__(self, tensorboard_dir, model_dir, batch_size, gpu_num, class_num, lr):
        """
        You can add more default params in here, or use **kwargs for convenience.

        :param tensorboard_dir:
        :param batch_size:
        :param gpu_num:
        :param class_num:
        :param lr:
        """
        self.tensorboard_dir = tensorboard_dir
        self. model_dir = model_dir
        self.batch_size = batch_size
        self.gpu_num = gpu_num
        self.class_num = class_num
        self.lr = lr

    def train(self):
        print "Model Stored in: ", self.tensorboard_dir
        print "Batch size of this network is: ", self.batch_size
