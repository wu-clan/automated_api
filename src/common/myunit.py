#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.common.log import log


class Unit(unittest.TestCase):
    """执行同步"""

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
    """执行异步"""

    async def asyncSetUp(self) -> None:
        pass

    async def asyncTearDown(self) -> None:
        pass

