#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import yaml

from src.common.log import log
from src.core.path_settings import YAML_FILE


class DoYaml:

    @staticmethod
    def read_yaml(filename):
        """
        读取 yaml 文件
        :param filename: 文件名
        :return:
        """
        _filename = os.path.join(YAML_FILE, filename)
        try:
            with open(_filename, encoding='utf-8') as f:
                if '---' in f.read():
                    return yaml.load_all(f.read(), Loader=yaml.FullLoader)
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except Exception as e:
            log.error(f'文件 {filename} 不存在\n{e}')
            raise e

    @staticmethod
    def write_yaml(filename, data, encoding='utf-8'):
        """
        写入内容到 yaml 文件
        :param filename: 文件名
        :param data: 数据
        :param encoding: 编码格式
        :return:
        """
        _filename = os.path.join(YAML_FILE, filename)
        try:
            with open(_filename, encoding=encoding, mode='w') as f:
                return yaml.dump(data, stream=f, allow_unicode=True)
        except Exception as e:
            log.error(f'file not found "{filename}"')
            raise e
