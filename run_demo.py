#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import sys
import time
import unittest

from DemoAPI.config import setting
from DemoAPI.db import test_data
from DemoAPI.models.newReport import new_report
from DemoAPI.models.sendmail import send_mail
from DemoAPI.models.writeexcel import WriteExcel
from DemoAPI.packages.HTMLTestRunner import HTMLTestRunner

sys.path.append(os.path.dirname(__file__))


def add_case(test_path=setting.TEST_CASE):
	"""加载所有的测试用例"""
	discover = unittest.defaultTestLoader.discover(test_path, pattern='*API.py')
	return discover


def run_case(all_case, result_path=setting.TEST_REPORT):
	"""执行所有的测试用例"""

	# 初始化接口测试数据
	test_data.init_data()

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = result_path + '/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
	                        title='发布会系统接口自动化测试报告',
	                        description='环境：windows 7 浏览器：chrome',
	                        tester='Jason')
	runner.run(all_case)
	fp.close()
	report = new_report(setting.TEST_REPORT)  # 调用模块生成最新的报告
	send_mail(report)  # 调用发送邮件模块


if __name__ == "__main__":
	cases = add_case()
	run_case(cases)
