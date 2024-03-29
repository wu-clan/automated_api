#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from concurrent.futures.thread import ThreadPoolExecutor

from src.common.test_report import add_testcase


def run_thread(suits, thread_num: int = 8):
    """
    多线程运行所有用例

    :param suits: 测试
    :param thread_num: 线程数
    :return:
    """
    res = unittest.TestResult()
    with ThreadPoolExecutor(max_workers=thread_num) as tp:
        for case in suits:
            tp.submit(case.run, result=res)
    return res


if __name__ == '__main__':
    test_suite = add_testcase()
    runner = run_thread(test_suite)
