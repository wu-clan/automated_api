#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.common.log import log


def log_current_req_data(data) -> None:
    """
    日志记录当前请求数据
    :return:
    """
    log.info(f"---------- use case being executed -> {data['ID']} ----------")
    log.info(f"request method: {data['method']}，request url: {data['url']}")
    log.info(f"request params: {data['params']}")
    log.info(f"request body type：{data['type']} , request content：{data['body']}")