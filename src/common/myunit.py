#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.common.log import log


class Unit(unittest.TestCase):
    """ 同步执行 """

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        log.info('new test start')

    def tearDown(self) -> None:
        log.info('this test end')

    @classmethod
    def tearDownClass(cls) -> None:
        log.info('全部测试同步执行完毕')


class AsyncUnit(unittest.IsolatedAsyncioTestCase):
    """ 异步执行, 同步请求/异步请求 都可用 """

    async def asyncSetUp(self) -> None:
        pass

    async def asyncTearDown(self) -> None:
        pass

