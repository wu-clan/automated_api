#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from loguru import logger

from src.core.settings import LOG_PATH


class Logger:
    # 判定文件夹
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)

    # 日志文件名称
    log_file = os.path.join(LOG_PATH, "api_test.log")

    # loguru日志
    logger.add(
        log_file,
        level="DEBUG",
        rotation='00:00',
        retention="7 days",
        encoding='utf-8',
        enqueue=True,
        backtrace=True,
        diagnose=True
    )
