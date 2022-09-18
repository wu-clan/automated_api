#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.common.log import log
from src.common.test_report import html_report, add_testcase
from src.utils.send_report.send_mail import SendMail

if __name__ == '__main__':
    try:
        """
        HTMLTestRunner 测试报告
        """
        test_suite = add_testcase()
        runner, fp, filename = html_report()
        runner.run(test_suite)
    except Exception as e:
        log.error('❌ 运行异常')
        raise e
    else:
        send_email = SendMail(filename)
        send_email.send()
