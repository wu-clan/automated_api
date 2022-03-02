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
        ax_excel: 通过excel文件参数发送httpx_request请求
        ax_yaml: 通过yaml文件参数发送httpx_request请求
        aio_excel: 通过yaml文件参数发送aiohttp_request请求
        aio_yaml: 通过yaml文件参数发送aiohttp_request请求
        '''
        """
        self.requestMethod = requestMethod

    def _sync_req(self, data):
        """
        excel同步请求参数集合
        :param data:
        :return:
        """
        self.method = data["method"]
        self.url = data["url"]
        if data["params"] == "" or data["params"] is None:
            self.params = None
        else:
            self.params = eval(data["params"])
        if data["headers"] == "" or data["headers"] is None:
            self.headers = None
        else:
            self.headers = dict(data["headers"])
        if data["body"] == "" or data["body"] is None:
            body_data = None
        else:
            body_data = eval(data["body"])
        if data["type"] == "data":
            self.body = body_data
        elif data["type"] == "json":
            self.body = json.dumps(body_data)
        else:
            self.body = body_data
        return [self.method, self.url, self.params, self.headers, self.body]

    def _async_req(self, data):
        """
        excel异步请求参数集合
        :param data:
        :return:
        """
        return self._sync_req(data)

    def send_sync_requests(self, data) -> Union[httpx_res, requests_res]:
        """
        发送同步请求
        :param data: 请求数据
        :return: response
        """
        err = ['requests', 'httpx']
        if self.requestMethod not in err:
            raise Exception(f'请求参数错误，仅 {err}')

        if self.requestMethod == 'requests':
            try:
                req = self._sync_req(data)
                # 消除安全警告
                requests.packages.urllib3.disable_warnings()
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                rq = requests.session().request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                                verify=settings.REQUEST_VERIFY, timeout=settings.REQUEST_TIMEOUT)
                return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise e

        if self.requestMethod == 'httpx':
            try:
                req = self._sync_req(data)
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                with httpx.Client(verify=settings.REQUEST_VERIFY, follow_redirects=True) as client:
                    rq = client.request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                        timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise e

    async def send_async_requests(self, data) -> Union[httpx_res, aiohttp_res]:
        """
        发送异步请求，如果接口服务器有速率限制，不建议使用
        :param data: 请求数据
        :return: response
        """
        err = ['async_httpx', 'aiohttp']
        if self.requestMethod not in err:
            raise Exception(f'请求参数错误，仅 {err}')
        if self.requestMethod == 'async_httpx':
            try:
                req = self._async_req(data)
                async with httpx.AsyncClient(verify=settings.REQUEST_VERIFY) as client:
                    rq = await client.request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                              timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise e

        if self.requestMethod == 'aiohttp':
            try:
                req = self._async_req(data)
                async with aiohttp.ClientSession() as session:
                    rq = await session.request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                               timeout=settings.REQUEST_TIMEOUT, ssl=settings.REQUEST_VERIFY)
                    return rq
            except Exception as e:
                log.error(f'请求异常: {e}')
                raise e


def sync_request(data):
    return SendRequests('requests').send_sync_requests(data)


def sync_httpx(data):
    return SendRequests('httpx').send_sync_requests(data)


async def async_httpx(data):
    rq = await SendRequests('async_httpx').send_async_requests(data)
    return rq


async def async_aiohttp(data):
    rq = await SendRequests('aiohttp').send_async_requests(data)
    return rq


__all__ = (
    'sync_request',
    'sync_httpx',
    # 'async_httpx',
    # 'async_aiohttp',
)
