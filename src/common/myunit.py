#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.common.log import log


class Unit(unittest.TestCase):
    """ 同步执行 """

    def __init__(self, *args, **kwargs):
        # 继承 unittest.TestCase 的__init__,尤为重要
        unittest.TestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        log.info('new test start')
        log.info(f'Start executing the test case: {self._testMethodName}')

    def tearDown(self) -> None:
        log.info('this test end')

    @classmethod
    def tearDownClass(cls) -> None:
        log.info('全部测试同步执行完毕')


class AsyncUnit(unittest.IsolatedAsyncioTestCase):
    """ 异步执行, 同步请求/异步请求 都可用 """

    def __init__(self, *args, **kwargs):
        # 继承 unittest.IsolatedAsyncioTestCase 的__init__,尤为重要
        unittest.IsolatedAsyncioTestCase.__init__(self, *args, **kwargs)

    async def asyncSetUp(self) -> None:
        log.info(f'Start executing the test case: {self._testMethodName}')

    async def asyncTearDown(self) -> None:
        pass

