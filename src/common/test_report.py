#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import unittest

from XTestRunner import HTMLTestRunner
from jinja2 import Template

from src.common.log import log
from src.core.conf import settings
from src.core.path_settings import HTML_REPORT, TEST_CASES, EMAIL_REPORT_TEMPLATE
from src.utils.time_control import get_current_time


def html_report():
    """
    HTML 测试报告
    """
    filename = os.path.join(HTML_REPORT, settings.RESULT_FILENAME + '_' + get_current_time() + '.html')
    try:
        if not os.path.exists(HTML_REPORT):
            os.makedirs(HTML_REPORT)
        fp = open(filename, 'wb')
    except Exception as e:
        log.error(f'{filename} 打开失败: {e}')
        raise e
    else:
        runner = HTMLTestRunner(
            stream=fp,
            title=settings.RESULT_TITLE,
            verbosity=2,
            tester=settings.TESTER_NAME,
            description=settings.RESULT_DESCRIPTION,
            language='zh-CN'
        )
        return runner, fp, filename


def add_testcase(path=TEST_CASES, rule='test_*.py'):
    """
    添加测试用例

    :param path: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(path, rule)
    return discover


def render_email_test_report(file=EMAIL_REPORT_TEMPLATE, **kwargs):
    """
    渲染邮箱测试报告

    :param file:
    :return:
    """
    with open(file, 'r', encoding='utf-8') as f:
        html = Template(f.read())

    return html.render(**kwargs)

