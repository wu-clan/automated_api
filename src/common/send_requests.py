#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import time
from typing import Union

import aiohttp
import httpx
import requests
from aiohttp import ClientResponse as aiohttp_res
from httpx import Response as httpx_res
from requests import Response as requests_res

from src.common.log import log
from src.core.conf import settings


class SendRequests(object):
    """发送请求数据"""

    def __init__(self, requestMethod: str):
        """
        :param requestMethod: 请求方式
        sync:
        '''
        excel: 通过excel文件参数发送request请求
        yaml: 通过yaml文件参数发送request请求
        httpx_excel: 通过excel文件参数发送httpx_request请求
        httpx_yaml: 通过yaml文件参数发送httpx_request请求
        '''
        async:
        '''
        httpx_excel: 通过excel文件参数发送httpx_request请求
        httpx_yaml: 通过yaml文件参数发送httpx_request请求
        aio_excel: 通过yaml文件参数发送aiohttp_request请求
        aio_yaml: 通过yaml文件参数发送aiohttp_request请求
        '''
        """
        self.requestMethod = requestMethod

    def send_sync_requests(self, data) -> Union[httpx_res, requests_res]:
        """
        发送同步请求
        :param data: 请求数据
        :return: response
        """
        err = ('excel' or 'yaml' or 'httpx_excel' or 'httpx_yaml')
        if self.requestMethod != err:
            raise Exception(f'请求参数错误，仅 {err}')
        if self.requestMethod == 'excel':
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
                rq = requests.session().request(method=method, url=url, headers=headers, params=params, data=body,
                                                verify=settings.REQUEST_VERIFY, timeout=settings.REQUEST_TIMEOUT)
                return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise
        if self.requestMethod == 'yaml':
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
                rq = requests.session().request(method=method, url=url, headers=headers, params=params, data=body,
                                                verify=settings.REQUEST_VERIFY, timeout=settings.REQUEST_TIMEOUT)
                return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise
        if self.requestMethod == 'httpx_excel':
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
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                with httpx.Client(verify=settings.REQUEST_VERIFY, follow_redirects=True) as client:
                    rq = client.request(method=method, url=url, headers=headers, params=params, data=body,
                                        timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise
        if self.requestMethod == 'httpx_yaml':
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
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                with httpx.Client(verify=settings.REQUEST_VERIFY, follow_redirects=True) as client:
                    rq = client.request(method=method, url=url, headers=headers, params=params, data=body,
                                        timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise

    async def send_async_requests(self, data) -> Union[httpx_res, aiohttp_res]:
        """
        发送异步请求，如果接口服务器有速率限制，不建议使用
        :param data: 请求数据
        :return: response
        """
        err = ('httpx_excel' or 'httpx_yaml' or 'aio_excel' or 'aio_yaml')
        if self.requestMethod != err:
            raise Exception(f'请求参数错误，仅 {err}')
        if self.requestMethod == 'httpx_excel':
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
                async with httpx.AsyncClient(verify=settings.REQUEST_VERIFY) as client:
                    rq = await client.request(method=method, url=url, headers=headers, params=params, data=body,
                                              timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise
        if self.requestMethod == 'httpx_yaml':
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
                async with httpx.AsyncClient(verify=settings.REQUEST_VERIFY) as client:
                    rq = await client.request(method=method, url=url, headers=headers, params=params, data=body,
                                              timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求发送失败\n{e}')
                raise
        if self.requestMethod == 'aio_excel':
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
                async with aiohttp.ClientSession() as session:
                    rq = await session.request(method=method, url=url, headers=headers, params=params, data=body,
                                               timeout=settings.REQUEST_TIMEOUT, ssl=settings.REQUEST_VERIFY)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise
        if self.requestMethod == 'aio_yaml':
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
                async with aiohttp.ClientSession() as session:
                    rq = await session.request(method=method, url=url, headers=headers, params=params, data=body,
                                               timeout=settings.REQUEST_TIMEOUT, ssl=settings.REQUEST_VERIFY)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise
