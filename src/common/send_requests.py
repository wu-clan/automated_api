#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import asyncio
import json
import time
from typing import Union

import aiohttp
import httpx
import requests
from aiohttp import ClientResponse as aiohttp_rq
from httpx import Response as httpx_rq
from requests import Response as requests_rq

from src.common.log import log
from src.core.conf import settings


class SendRequests(object):
    """ 发送请求 """

    def __init__(self, requestMethod: str = None):
        """
        :param requestMethod: 请求方式
        """
        self.requestMethod = requestMethod

    @staticmethod
    def _sync_data(data):
        """
        excel同步请求数据
        :param data:
        :return:
        """
        method = data["method"]
        url = data["url"]
        if data["params"] == "" or data["params"] is None:
            params = None
        else:
            params = eval(data["params"])
        if data["headers"] == "" or data["headers"] is None:
            headers = None
        else:
            headers = dict(data["headers"])
        if data["body"] == "" or data["body"] is None:
            body_data = None
        else:
            body_data = eval(data["body"])
        if data["type"] == "data":
            body = body_data
        elif data["type"] == "json":
            body = json.dumps(body_data)
        else:
            body = body_data
        return [method, url, params, headers, body]

    async def _async_data(self, data):
        """
        excel异步请求数据
        :return:
        """
        return await asyncio.get_event_loop().run_in_executor(None, self._sync_data, data)

    def _send_sync_requests(self, data) -> Union[httpx_rq, requests_rq]:
        """
        发送同步请求
        :param data: 请求数据
        :return: response
        """
        err = ['requests', 'httpx']
        if self.requestMethod not in err:
            raise ValueError(f'请求参数错误，仅 {err}')

        if self.requestMethod == 'requests':
            try:
                req = self._sync_data(data)
                # 消除安全警告
                requests.packages.urllib3.disable_warnings()
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                rq = requests.session().request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                                verify=settings.REQUEST_VERIFY, timeout=settings.REQUEST_TIMEOUT)
                return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

        if self.requestMethod == 'httpx':
            try:
                req = self._sync_data(data)
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                with httpx.Client(verify=settings.REQUEST_VERIFY, follow_redirects=True) as client:
                    rq = client.request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                        timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

    async def _send_async_requests(self, data) -> Union[httpx_rq, aiohttp_rq]:
        """
        发送异步请求，如果接口服务器有速率限制，不建议使用
        :param data: 请求数据
        :return: response
        """
        err = ['async_httpx', 'aiohttp']
        if self.requestMethod not in err:
            raise ValueError(f'请求参数错误，仅 {err}')

        if self.requestMethod == 'async_httpx':
            try:
                req = await self._async_data(data)
                # 请求间隔
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                async with httpx.AsyncClient(verify=settings.REQUEST_VERIFY) as client:
                    rq = await client.request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                              timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

        if self.requestMethod == 'aiohttp':
            try:
                req = await self._async_data(data)
                # 请求间隔
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                async with aiohttp.ClientSession() as session:
                    rq = await session.request(method=req[0], url=req[1], params=req[2], headers=req[3], data=req[4],
                                               timeout=settings.REQUEST_TIMEOUT, ssl=settings.REQUEST_VERIFY)
                    return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

    def sync_request(self, data) -> requests_rq:
        """
        通过 request 发送同步请求
        :param data:
        :return:
        """
        self._req_log(data)
        self.requestMethod = 'requests'
        return self._send_sync_requests(data)

    def sync_httpx(self, data) -> httpx_rq:
        """
        通过 httpx 发送同步请求
        :param data:
        :return:
        """
        self._req_log(data)
        self.requestMethod = 'httpx'
        return self._send_sync_requests(data)

    async def async_httpx(self, data) -> httpx_rq:
        """
        通过 httpx 发送异步请求
        :param data:
        :return:
        """
        await asyncio.get_event_loop().run_in_executor(None, self._req_log, data)
        self.requestMethod = 'async_httpx'
        rq = await self._send_async_requests(data)
        return rq

    async def async_aiohttp(self, data) -> aiohttp_rq:
        """
        通过 aiohttp 发送异步请求
        :param data:
        :return:
        """
        await asyncio.get_event_loop().run_in_executor(None, self._req_log, data)
        self.requestMethod = 'aiohttp'
        rq = await self._send_async_requests(data)
        return rq

    @staticmethod
    def _req_log(data):
        log.info(f"正在调用的数据ID: --> {data['ID']}")
        log.info(f"请求 method: {data['method']}")
        log.info(f"请求 url: {data['url']}")
        log.info(f"请求 params: {data['params']}")
        log.info(f"请求 body 类型：{data['type']}")
        log.info(f"请求 body：{data['body']}")


send_request = SendRequests()

__all__ = [
    'send_request'
]
