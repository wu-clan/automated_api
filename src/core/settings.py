#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from src.common.doconfIni import DoConfIni

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 定义变量
read_config = DoConfIni()
config = os.path.join(BASE_DIR, 'core', 'config.ini')

# tester
TESTER = read_config.get_conf_value(config, 'tester', 'name')

# result
RESULT_TITLE = read_config.get_conf_value(config, 'result', 'title')

# DB
DB_HOST = read_config.get_conf_value(config, 'db', 'host')
DB_PORT = read_config.get_conf_value(config, 'db', 'port')
DB_USER = read_config.get_conf_value(config, 'db', 'user')
DB_PASSWORD = read_config.get_conf_value(config, 'db', 'password')
DB_DATABASE = read_config.get_conf_value(config, 'db', 'db_database')
DB_CHARSET = read_config.get_conf_value(config, 'db', 'db_charset')

# EMAIL
EMAIL_HOST_SERVER = read_config.get_conf_value(config, 'email', 'host_server')
EMAIL_FROM = read_config.get_conf_value(config, 'email', 'from')
EMAIL_TO = read_config.get_conf_value(config, 'email', 'to')
EMAIL_USER = read_config.get_conf_value(config, 'email', 'user')
EMAIL_PASSWORD = read_config.get_conf_value(config, 'email', 'password')

# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR, 'data', 'DemoAPITestCase.xlsx')

# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR, 'report', 'excel_report', 'DemoAPITestCase.xlsx')

# 测试用例报告路径
TEST_REPORT_PATH = os.path.join(BASE_DIR, "report", 'html_report')

# 测试用例路径
TEST_CASE_PATH = os.path.join(BASE_DIR, 'testcase')

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
