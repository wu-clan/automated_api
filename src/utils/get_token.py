#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

_url: str = 'http://127.0.0.1:8000/v1/login'
_data: dict = {'username': '1', 'password': '1'}
_headers: dict = {'Content-Type': 'application/x-www-form-urlencoded'}
# 返回请求的token变量名
_token_name: str = 'access_token'


def get_token() -> None:
    """
    获取token
    :return:
    """
    try:
        response = requests.post(url=_url, data=_data, headers=_headers, ).json()
    except Exception as e:
        print(f'获取 token 失败\n{e}')
    else:
        token = response[_token_name]
        print(f'获取 token 成功: {token}')
