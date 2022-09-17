#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import yaml

from src.common.log import log
from src.core.path_settings import YAML_FILE, YAML_REPORT
from src.utils.time_control import get_current_time


def read_yaml(filename: str):
    """
    读取 yaml 文件

    :return:
    """
    _filename = os.path.join(YAML_FILE, filename)
    try:
        with open(_filename, encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)
    except Exception as e:
        log.error(f'文件 {filename} 不存在: {e}')
        raise e


def write_yaml(filename=f'APITestResult_{get_current_time()}.yaml', *, data=None, mode='a', encoding='utf-8'):
    """
    写入内容到 yaml 文件

    :param filename: 保存报告的文件名
    :param data: 数据
    :param mode:
    :param encoding: 编码格式
    :return:
    """
    if not os.path.exists(YAML_REPORT):
        os.mkdir(YAML_REPORT)
    _filename = os.path.join(YAML_REPORT, filename)
    try:
        with open(_filename, encoding=encoding, mode=mode) as f:
            result = yaml.dump(data, stream=f, allow_unicode=True)
    except Exception as e:
        log.error(f'写入文件 "{_filename}" 错误: {e}')
        raise e
    else:
        log.info('写入yaml测试报告成功')
        return result


def get_yaml(filename: str):
    """
    获取 yaml 测试数据文件

    :param filename:
    :return:
    """
    return os.path.join(YAML_FILE, filename)
