#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import unittest

# 导入配置文件中定义的测试报告的路径
# 导入配置文件中定义的测试用例的路径
from conf.settings import REPORT_PATH, TESTCASE_PATH
from lib.HTMLTestReportCN import HTMLTestRunner as hr2
# 导入报告模板
from lib.HTMLTestRunner import HTMLTestRunner as hr1

# 获取项目的根目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)
sys.path.insert(0, path)

# 自动根据测试用例的路径匹配查找测试用例文件（*.py）,并将查找到的测试用例组装到测试套件中
suit = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')
# print(suit)

if __name__ == '__main__':
    # 获取当前时间并指定时间格式
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 创建报告文件
    fp = open(REPORT_PATH + now + "_report.html", 'wb')
    # fp = open(REPORT_PATH + "_report_all.html", 'wb')
    runner = hr2(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'win10 64',
        tester="wu")
    runner.run(suit)
    fp.close()

    # import os, sys, re
    # path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # sys.path.insert(0, path)
    # from conf.settings import DATA_PATH
    #
    # dirs = os.listdir(DATA_PATH)
    # print(dirs)  # ['testcase.xlsx', '~$testcase.xlsx']
    # for i in range(len(dirs)):
    #     path = os.path.join(DATA_PATH, dirs[i])  # 遍历目录下的所有文件
    #     print(path)
    #     if os.path.isfile(path):
    #         list_name = re.findall('test(.*?).xls', path)
    #         name = list_name[0]
    #         print(name)
