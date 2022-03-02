#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from src.core.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例参数 yaml 文件
YAML_FILE = os.path.join(BASE_DIR, 'data')

# 测试用例参数 xlsx 文件
XLSX_FILE = os.path.join(BASE_DIR, 'data')

# 测试用例参数文件
TEMPLATE_XLSX_FILE = os.path.join(BASE_DIR, 'data', 'DemoAPITestCase.xlsx')

# 测试用例路径
TEST_CASES = os.path.join(BASE_DIR, 'testcase', settings.PROJECT)

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, 'log')

# EXCEL测试报告
EXCEL_REPORT = os.path.join(BASE_DIR, 'report', 'excel_report')

# HTML测试报告
HTML_REPORT = os.path.join(BASE_DIR, 'report', 'html_report')

# YAML测试报告
YAML_REPORT = os.path.join(BASE_DIR, 'report', 'yaml_report')
