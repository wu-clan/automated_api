#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date : 2021-04-14
# @PRODUCT_NAME :  PyCharm


import unittest

from src.common.html_report import html_report
from src.testcase.test.testAPI import Demo_API


class RunTcClass:

    # 重定向类为 TestSuite()
    def __init__(self):
        self.suites = unittest.TestLoader()
        self.suit = unittest.TestSuite()

    def test_class(self, testCaseClass):
        """
        :param testCaseClass: 引入的类名
        """
        suites = self.suites.loadTestsFromTestCase(testCaseClass)
        self.suit.addTest(suites)


if __name__ == '__main__':
    suite_tc = RunTcClass()

    # from 引入类，在这里（）内直接填入即可
    suite_tc.test_class(Demo_API)

    # 1.不输出到测试报告
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_tc.suit)

    # 2.输出到HTML测试报告
    # runner, fp, filename = html_report()
    # runner.run(suite_tc.suit)
