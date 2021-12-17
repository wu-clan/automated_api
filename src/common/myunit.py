#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

import requests

from src.common.log import log
from src.common.read_yaml import ReadYaml

requestInfo = ReadYaml().read_yaml('get_token.yaml')['login']


class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        url = requestInfo['url']
        data = requestInfo['data']
        headers = requestInfo['headers']
        response = requests.post(url=url, data=data, headers=headers,).json()
        # 全局变量token
        global token
        token = response[requestInfo['token_name']]
        log.info(f'获取全局 token 成功: {token}')

    def setUp(self) -> None:
        log.info('new test start')

    def tearDown(self) -> None:
        log.info('this test end')

    @classmethod
    def tearDownClass(cls) -> None:
        log.info('全部测试执行完毕')

