#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import yaml

from src.common.log import log
from src.core.path_settings import YAML_FILE


class ReadYaml:

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
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except Exception as e:
            log.error(f'文件 {filename} 不存在\n{e}')
            raise e
