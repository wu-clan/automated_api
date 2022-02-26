#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time

import requests

from src.common.log import log
from src.core.conf import settings


class SendRequests(object):
    """发送请求数据"""

    @staticmethod
    def send_requests_by_excel(data):
        """
        使用excel参数发送请求
        :param data: 请求参数
        :return:
        """
        try:
            method = data["method"]
            url = data["url"]
            if data["params"] == "":
                params = None
            else:
                params = eval(data["params"])
            if data["headers"] == "":
                headers = None
            else:
                headers = dict(data["headers"])
            if data["body"] == "":
                body_data = None
            else:
                body_data = eval(data["body"])
            if data["type"] == "data":
                body = body_data
            elif data["type"] == "json":
                body = json.dumps(body_data)
            else:
                body = body_data
            # 消除安全警告
            requests.packages.urllib3.disable_warnings()
            # 请求间隔
            time.sleep(settings.REQUEST_INTERVAL)
            # 发送请求
            rq = requests.session().request(method=method, url=url, headers=headers, params=params, data=body,
                                            verify=False, timeout=settings.REQUEST_TIMEOUT)
            return rq
        except Exception as e:
            log.error(f'请求发送失败\n{e}')

    @staticmethod
    def send_requests_by_yaml(data):
        """
        使用yaml参数发送请求
        :param data: 请求参数
        :return:
        """
        try:
            method = data["method"]
            url = data["url"]
            if data["params"] is None:
                params = None
            else:
                params = eval(data["params"])
            if data["headers"] is None:
                headers = None
            else:
                headers = dict(data["headers"])
            if data["body"] is None:
                body_data = None
            else:
                body_data = eval(data["body"])
            if data["type"] == "data":
                body = body_data
            elif data["type"] == "json":
                body = json.dumps(body_data)
            else:
                body = body_data
            # 消除安全警告
            requests.packages.urllib3.disable_warnings()
            # 请求间隔
            time.sleep(settings.REQUEST_INTERVAL)
            # 发送请求
            rq = requests.session().request(method=method, url=url, headers=headers, params=params, data=body,
                                            verify=False, timeout=settings.REQUEST_TIMEOUT)
            return rq
        except Exception as e:
            log.error(f'请求发送失败\n{e}')
