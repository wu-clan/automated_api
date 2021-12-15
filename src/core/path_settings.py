#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from src.common.do_confIni import DoConfIni

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 定义变量
read_config = DoConfIni()
config = os.path.join(BASE_DIR, 'core', 'config.ini')

# tester
TESTER = read_config.get_conf_value(config, 'tester', 'name')

# result
RESULT_TITLE = read_config.get_conf_value(config, 'result', 'title')
DESCRIPTION = read_config.get_conf_value(config, 'result', 'description')

# DB
DB_HOST = read_config.get_conf_value(config, 'db', 'host')
DB_PORT = read_config.get_conf_value(config, 'db', 'port')
DB_USER = read_config.get_conf_value(config, 'db', 'user')
DB_PASSWORD = read_config.get_conf_value(config, 'db', 'password')
DB_DATABASE = read_config.get_conf_value(config, 'db', 'database')
DB_CHARSET = read_config.get_conf_value(config, 'db', 'charset')

# EMAIL
EMAIL_HOST_SERVER = read_config.get_conf_value(config, 'email', 'host_server')
EMAIL_FROM = read_config.get_conf_value(config, 'email', 'from')
EMAIL_TO = read_config.get_conf_value(config, 'email', 'to')
EMAIL_USER = read_config.get_conf_value(config, 'email', 'user')
EMAIL_PASSWORD = read_config.get_conf_value(config, 'email', 'password')
EMAIL_PORT = read_config.get_conf_value(config, 'email', 'port')

# 测试用例参数模板文件
YAML_FILE = os.path.join(BASE_DIR, 'data')

# 测试用例参数模板文件
TEMPLATE_FILE = os.path.join(BASE_DIR, 'data', 'DemoAPITestCase.xlsx')

# excel测试报告文件
EXCEL_RESULT = os.path.join(BASE_DIR, 'report', 'excel_report', 'APITestResult.xlsx')

# HTML测试报告路径
HTML_REPORT = os.path.join(BASE_DIR, "report", 'html_report')

# 测试用例文件夹名
FILE_NAME = read_config.get_conf_value(config, 'project', 'project')

# 测试用例路径
TEST_CASES = os.path.join(BASE_DIR, 'testcase', FILE_NAME)

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
