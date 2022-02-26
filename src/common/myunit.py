#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.common.log import log


class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        log.info('new test start')

    def tearDown(self) -> None:
        log.info('this test end')

    @classmethod
    def tearDownClass(cls) -> None:
        log.info('全部测试执行完毕')

