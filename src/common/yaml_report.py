#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

import yaml

from src.common.log import log
from src.core.path_settings import YAML_REPORT


class WriteYaml:

    curr_time = time.strftime('%Y-%m-%d %H_%M_%S')

    @staticmethod
    def write_yaml(filename=f'APITestResult_{curr_time}.yaml', data=None, encoding='utf-8'):
        """
        写入内容到 yaml 文件
        :param filename: 保存报告的文件名
        :param data: 数据
        :param encoding: 编码格式
        :return:
        """
        if not os.path.exists(YAML_REPORT):
            os.mkdir(YAML_REPORT)
        _filename = os.path.join(YAML_REPORT, filename)
        try:
            with open(_filename, encoding=encoding, mode='a') as f:
                return yaml.dump(data, stream=f, allow_unicode=True)
        except Exception as e:
            log.error(f'写入文件 "{_filename}" 错误\n{e}')
            raise e


