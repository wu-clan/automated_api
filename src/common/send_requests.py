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
    def __sync_data(data):
        """
        同步请求数据
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

    async def __async_data(self, data):
        """
        异步请求数据
        :return:
        """
        return await asyncio.get_event_loop().run_in_executor(None, self.__sync_data, data)

    def __send_sync_requests(self, data) -> Union[httpx_rq, requests_rq]:
        """
        发送同步请求
        :param data: 请求数据
        :return: response
        """
        err = ['requests', 'httpx']
        if self.requestMethod not in err:
            raise ValueError(f'请求参数错误，仅 {err}')

        # 记录请求参数
        req_args = self.__sync_data(data)
        req_method = req_args[0]
        req_url = req_args[1]
        req_params = req_args[2]
        req_headers = req_args[3]
        req_data = req_args[4]

        if self.requestMethod == 'requests':
            try:
                # 消除安全警告
                requests.packages.urllib3.disable_warnings()
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                rq = requests.session().request(method=req_method, url=req_url, params=req_params, headers=req_headers,
                                                data=req_data, timeout=settings.REQUEST_TIMEOUT,
                                                verify=settings.REQUEST_VERIFY)
                return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

        if self.requestMethod == 'httpx':
            try:
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                with httpx.Client(verify=settings.REQUEST_VERIFY, follow_redirects=True) as client:
                    rq = client.request(method=req_method, url=req_url, params=req_params, headers=req_headers,
                                        data=req_data, timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

    async def __send_async_requests(self, data) -> Union[httpx_rq, aiohttp_rq]:
        """
        发送异步请求，如果接口服务器有速率限制，不建议使用
        :param data: 请求数据
        :return: response
        """
        err = ['async_httpx', 'aiohttp']
        if self.requestMethod not in err:
            raise ValueError(f'请求参数错误，仅 {err}')

        # 记录请求参数
        req_args = await self.__async_data(data)
        req_method = req_args[0]
        req_url = req_args[1]
        req_params = req_args[2]
        req_headers = req_args[3]
        req_data = req_args[4]

        if self.requestMethod == 'async_httpx':
            try:
                # 请求间隔
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                async with httpx.AsyncClient(verify=settings.REQUEST_VERIFY) as client:
                    rq = await client.request(method=req_method, url=req_url, params=req_params, headers=req_headers,
                                              data=req_data, timeout=settings.REQUEST_TIMEOUT)
                    return rq
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

        if self.requestMethod == 'aiohttp':
            try:
                # 请求间隔
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                async with aiohttp.ClientSession() as session:
                    rq = await session.request(method=req_method, url=req_url, params=req_params, headers=req_headers,
                                               data=req_data, timeout=settings.REQUEST_TIMEOUT,
                                               ssl=settings.REQUEST_VERIFY)
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
        return self.__send_sync_requests(data)

    def sync_httpx(self, data) -> httpx_rq:
        """
        通过 httpx 发送同步请求
        :param data:
        :return:
        """
        self._req_log(data)
        self.requestMethod = 'httpx'
        return self.__send_sync_requests(data)

    async def async_httpx(self, data) -> httpx_rq:
        """
        通过 httpx 发送异步请求
        :param data:
        :return:
        """
        await asyncio.get_event_loop().run_in_executor(None, self._req_log, data)
        self.requestMethod = 'async_httpx'
        rq = await self.__send_async_requests(data)
        return rq

    async def async_aiohttp(self, data) -> aiohttp_rq:
        """
        通过 aiohttp 发送异步请求
        :param data:
        :return:
        """
        await asyncio.get_event_loop().run_in_executor(None, self._req_log, data)
        self.requestMethod = 'aiohttp'
        rq = await self.__send_async_requests(data)
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
