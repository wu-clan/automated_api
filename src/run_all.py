# -*- coding: utf-8 -*-
"""
Code description：自动化测试所有
"""
import unittest

from src.common.html_report import html_report
from src.common.log import log
from src.core.path_settings import TEST_CASES
from src.utils.send_mail import send_email

if __name__ == '__main__':
    try:
        '''
		HTMLTestRunner 测试报告
		'''
        test_suite = unittest.defaultTestLoader.discover(TEST_CASES, 'test*.py')
        runner, fp, fileName = html_report()
        runner.run(test_suite)
    except Exception as e:
        log.error('运行出错！！！请检查！！！')
        raise e
    else:
        send_email.send()
