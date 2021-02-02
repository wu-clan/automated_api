#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

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

# 把path加入环境变量，0表示放在最前面，因为python解释器会按照列表顺序去依次到每个目录下去匹配你要导入的模块名，
# 只要在一个目录下匹配到了该模块名，就立刻导入，不再继续往后找
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
        title=u'测试提升圈项目实战接口自动化测试报告',
        description=u'测试报告也可访问测试服务器查看，地址：http://<自动化测试服务器IP>:8787/',
        tester="全栈测试笔记")
    runner.run(suit)
    fp.close()

    #     import os, sys, re
    #     path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     sys.path.insert(0, path)
    #     from conf.settings import DATA_PATH
    #
    #     dirs = os.listdir(DATA_PATH)
    #     print(dirs)  # ['testcase.xlsx', '~$testcase.xlsx']
    #     for i in range(len(dirs)):
    #         path = os.path.join(DATA_PATH, dirs[i])  # 遍历目录下的所有文件
    #         print(path)
    #         if os.path.isfile(path):
    #             list_name = re.findall('test(.*?).xls', path)
    #             name = list_name[0]
    #             print(name)
