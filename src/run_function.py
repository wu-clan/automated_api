# -*- coding: utf-8 -*-
"""
Code description：可单独的测试
"""

import unittest

from src.common.html_report import html_report
from src.testcase.test.testAPI import Demo_API


class RunTcScript:

    # 重定向类为 TestSuite()
    def __init__(self):
        self.suite = unittest.TestSuite()

    def test_function(self, testClass, testcase):
        """
        :param testClass: 引入的类名
        :param testcase: 函数名: str
        :return:
        """
        self.suite.addTest(testClass(testcase))


if __name__ == '__main__':
    # suite
    suite_tc = RunTcScript()

    '''用例'''
    suite_tc.test_function(Demo_API, 'test_api1')

    # 1.不输出到测试报告
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_tc.suite)

    # 2.输出到HTML测试报告
    # runner, fp, filename = html_report()
    # runner.run(suite_tc.suite)
