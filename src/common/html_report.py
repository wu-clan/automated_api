#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src.common.log import log
from src.core.conf import settings
from src.core.path_settings import HTML_REPORT
from src.packages.TestRunner.HTMLTestRunner import HTMLTestRunner


def html_report():
    """
    HTML 测试报告
    :return:
    """
    curr_time = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = HTML_REPORT + '\\' + settings.RESULT_FILENAME + '_' + curr_time + '.html'
    try:
        if not os.path.exists(HTML_REPORT):
            os.makedirs(HTML_REPORT)
        fp = open(filename, 'wb')
    except Exception as e:
        log.error(f'{filename} 打开失败\n{e}')
        raise e
    else:
        runner = HTMLTestRunner(stream=fp,
                                title=settings.RESULT_TITLE,
                                verbosity=2,
                                tester=settings.TESTER_NAME,
                                description=settings.RESULT_DESCRIPTION)
        log.success('正在使用-html测试报告方式-进行测试')
        return runner, fp, filename
