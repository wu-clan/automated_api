#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import asyncio
import json
import platform
import time

import aiohttp
import asyncer
import httpx
import requests

from src.common.log import log
from src.core.conf import settings


class SendRequests:
    """ 发送请求 """

    @staticmethod
    def __sync_data(data):
        """
        同步请求数据

        :param data:
        :return:
        """
        method = data["method"]
        url = data["url"]
        params = None if data["params"] == "" or data["params"] is None else eval(data["params"])
        headers = None if data["headers"] == "" or data["headers"] is None else dict(data["headers"])
        body_data = None if data["body"] == "" or data["body"] is None else eval(data["body"])
        info = {
            'method': method,
            'url': url,
            'params': params,
            'headers': headers,
            'data': body_data if data['type'] != 'json' else None,
            'json': json.dumps(body_data) if data['type'] == 'json' else None
        }
        return info

    async def __async_data(self, data):
        """
        异步请求数据

        :param data:
        :return:
        """
        return await asyncer.asyncify(self.__sync_data)(data)

    def send_sync_request(self, data, *, request_engin: str = 'requests', **kwargs):
        """
        发送同步请求

        :param data: 请求数据
        :param request_engin:
        :return: response
        """
        engin = ['requests', 'httpx']
        if request_engin not in engin:
            raise ValueError(f'请求发起失败，请使用合法的请求引擎')

        request_args = self.__sync_data(data)

        self.log_request_up(data)

        if request_engin == 'requests':
            try:
                # 消除安全警告
                requests.packages.urllib3.disable_warnings()  # noqa
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                response = requests.session().request(
                    **request_args,
                    timeout=settings.REQUEST_TIMEOUT,
                    verify=settings.REQUEST_VERIFY,
                    **kwargs
                )
                return response
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e
        elif request_engin == 'httpx':
            try:
                # 请求间隔
                time.sleep(settings.REQUEST_INTERVAL)
                with httpx.Client(verify=settings.REQUEST_VERIFY, follow_redirects=True) as client:
                    response = client.request(
                        **request_args,
                        timeout=settings.REQUEST_TIMEOUT,
                        **kwargs
                    )
                    return response
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

    async def send_async_request(self, data, *, request_engin: str = 'httpx', **kwargs):
        """
        发送异步请求

        :param data: 请求数据
        :param request_engin:
        :return: response
        """
        engin = ['httpx', 'aiohttp']
        if request_engin not in engin:
            raise ValueError(f'请求发起失败，请使用合法的请求引擎')

        request_args = await self.__async_data(data)

        await asyncer.asyncify(self.log_request_up)(data)

        if request_engin == 'httpx':
            try:
                # 请求间隔
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                async with httpx.AsyncClient(verify=settings.REQUEST_VERIFY) as client:
                    response = await client.request(
                        **request_args,
                        timeout=settings.REQUEST_TIMEOUT,
                        **kwargs
                    )
                    return response
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e
        elif request_engin == 'aiohttp':
            # 不建议使用 aiohttp, 他很蠢
            # 如果你喜欢用, 在触发一个不影响程序的错误时: RuntimeError: Event loop is closed
            # 请查看 issue -> https://github.com/aio-libs/aiohttp/issues/4324
            try:
                # 请求间隔
                await asyncio.sleep(settings.REQUEST_INTERVAL)
                async with aiohttp.ClientSession() as session:
                    response = await session.request(
                        **request_args,
                        timeout=settings.REQUEST_TIMEOUT,
                        ssl=settings.REQUEST_VERIFY,
                        **kwargs
                    )
                    return response
            except Exception as e:
                log.error(f'请求异常: \n {e}')
                raise e

    @staticmethod
    def log_request_up(data):
        log.info(f"正在调用的数据ID: --> {data['ID']}")
        log.info(f"请求 method: {data['method']}")
        log.info(f"请求 url: {data['url']}")
        log.info(f"请求 params: {data['params']}")
        log.info(f"请求 body 类型：{data['type']}")
        log.info(f"请求 body：{data['body']}")


send_request = SendRequests()
