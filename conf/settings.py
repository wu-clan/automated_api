#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义测试用例的目录路径
TESTCASE_PATH = os.path.join(BASE_PATH, 'test_case')
# 定义测报告的目录路径
REPORT_PATH = os.path.join(BASE_PATH, 'report/')
# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH, 'log/log.txt')
# 定义测试数据的目录路径
DATA_PATH = os.path.join(BASE_PATH, 'data')


# project env
HOST_INFO = {
    'dev': 'http://127.0.0.1:9999',
    'test': 'http://127.0.0.1:9999',
    'preProduct': 'http://127.0.0.1:9999'
}

# 当前要运行的sheet名
# SHEET_NAME = "lc"
SHEET_NAME = "Sheet1"

# sheet名及索引
SHEET_INFO = {
    'Sheet1': 0
}

PROJECT_IP = '127.0.0.1:8091'


# mysql数据库的连接信息
MYSQL_HOST = ''
MYSQL_PORT = 3806
MYSQL_DB_USER = 'root'
MYSQL_DB_PASSWORD = ''
MYSQL_DB_NAME = 'qzcsbj'

# redis数据库的连接信息
# r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='qzcsbj@redis666')
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 'qzcsbj@redis666'

# print(BASE_PATH)
# print(TESTCASE_PATH)
# print(REPORT_PATH)
# print(LOG_PATH)

# 参数替换，获取key
PATTERN = '\$\{(.*?)\}'
