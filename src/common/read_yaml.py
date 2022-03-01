#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import yaml

from src.common.log import log
from src.core.path_settings import YAML_FILE


class ReadYaml:
    """读取yaml文件数据"""

    def __init__(self, filename):
        """
        :param filename: 文件名
        """
        self.filename = filename

    def read_yaml(self):
        """
        读取 yaml 文件
        :return:
        """
        _filename = os.path.join(YAML_FILE, self.filename)
        try:
            with open(_filename, encoding='utf-8') as f:
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except Exception as e:
            log.error(f'文件 {self.filename} 不存在\n{e}')
            raise e
