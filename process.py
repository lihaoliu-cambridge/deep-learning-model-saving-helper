#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from preprocessing.auto_generate_tf_log_dir import genarate_tf_log_dir
from model.resnet import Resnet
import logging
import codecs
import yaml
import os
import re

__author__ = 'Liu Lihao'

logger = logging.getLogger()


def load_config(config_file_path):
    if not os.path.isfile(config_file_path):
        raise IOError('Config file {} not existed.'.format(config_file_path))

    with codecs.open(config_file_path, mode='r', encoding='utf-8') as config_file:
        config_dict = yaml.load(config_file)
        return config_dict


def process(args_config_file_path):
    # 1.get config args
    args_config = load_config(args_config_file_path)

    # 2.get tf log dir automatically from config args
    log_dir_params = args_config["log_dir_params"]

    pattern, default_pattern = log_dir_params["pattern"], log_dir_params["default_pattern"]
    if pattern is None or len(pattern) == 0:
        pattern = default_pattern

    tensorboard_dir, model_dir = genarate_tf_log_dir(args_config_file_path,
                                                     log_dir_params["tensorboard_dir"],
                                                     log_dir_params["model_dir"],
                                                     log_dir_params["note_dir"],
                                                     log_dir_params["self_increasing_mode"],
                                                     pattern)

    # 3.get running params from config args
    running_params = args_config["running_params"]
    batch_size = int(running_params["batch_size"])
    gpu_num = int(running_params["gpu_num"])
    class_num = int(running_params["class_num"])
    lr = float(running_params["lr"])

    # 4.use params to initialize network
    resnet = Resnet(tensorboard_dir, model_dir, batch_size, gpu_num, class_num, lr)

    # todo: 5. train your model
    resnet.train()


if __name__ == '__main__':
    process("./conf/args.yaml")
