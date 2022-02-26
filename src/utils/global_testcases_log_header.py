#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.common.log import log


def global_log(data) -> None:
    """
    全局测试用例请求统一日志头
    :return:
    """
    log.info(f"---------- use case being executed -> {data['ID']} ----------")
    log.info(f"request method: {data['method']}，request url: {data['url']}")
    log.info(f"request params: {data['params']}")
    log.info(f"request body type：{data['type']} , request content：{data['body']}")