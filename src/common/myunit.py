#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.common.log import log


class Unit(unittest.TestCase):
    """ 同步执行 """

    def __init__(self, *args, **kwargs):
        # 继承 unittest.TestCase 的__init__,尤为重要
        super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        log.info(f'----------------- Running case: {self._testMethodName} -----------------')

    def tearDown(self) -> None:
        log.info('end')

    @classmethod
    def tearDownClass(cls) -> None:
        pass


class AsyncUnit(unittest.IsolatedAsyncioTestCase):
    """ 异步执行 """

    def __init__(self, *args, **kwargs):
        # 继承 unittest.IsolatedAsyncioTestCase 的__init__,尤为重要
        super().__init__(*args, **kwargs)

    async def asyncSetUp(self) -> None:
        log.info(f'----------------- Running case: {self._testMethodName} -----------------')

    async def asyncTearDown(self) -> None:
        log.info('end')
