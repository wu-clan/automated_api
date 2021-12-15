#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

from src.common.log import log
from src.core.path_settings import DESCRIPTION, HTML_REPORT, RESULT_TITLE, TESTER
from src.packages.TestRunner.HTMLTestRunner import HTMLTestRunner


def html_report():
    """
    HTML 测试报告
    :return:
    """
    curr_time = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = HTML_REPORT + '\\' + RESULT_TITLE + '_' + curr_time + '.html'
    try:
        fp = open(filename, 'wb')
    except Exception as e:
        log.error(f'{filename} 打开失败\n{e}')
        raise e
    else:
        runner = HTMLTestRunner(stream=fp,
                                title=RESULT_TITLE,
                                verbosity=2,
                                tester=TESTER,
                                description=DESCRIPTION)
        log.success('html测试报告生成成功')
        return runner, fp, filename
