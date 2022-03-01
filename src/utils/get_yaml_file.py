#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from src.core.path_settings import YAML_FILE


def get_yaml(filename: str):
    """
    获取yaml测试数据文件
    :param filename:
    :return:
    """
    return os.path.join(YAML_FILE, filename)
