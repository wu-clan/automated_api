#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import Union, List

from pydantic import BaseSettings


class Settings(BaseSettings):
    # 项目目录名
    PROJECT: str = 'test'

    # 测试人员名称
    TESTER_NAME: str = '123'

    # HTML测试报告
    RESULT_FILENAME: str = 'html测试报告'
    RESULT_TITLE: str = '重新整理框架'
    RESULT_DESCRIPTION: str = '接口自动化测试'

    # 数据库
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_USER: str = 'root'
    DB_PASSWORD: str = '123456'
    DB_DATABASE: str = 'auto_api'
    DB_CHARSET: str = 'utf8mb4'

    # 邮件发送
    EMAIL_HOST_SERVER: str = 'smtp.163.com'
    EMAIL_TIMEOUT: int = 5
    EMAIL_PORT: int = 25
    EMAIL_USER: str = '222@126.com'
    EMAIL_PASSWORD: str = '********'
    EMAIL_TO: Union[str, List] = '********'

    # 发送请求
    REQUEST_TIMEOUT: Union[int, float, List] = 5
    REQUEST_INTERVAL: Union[int, float] = 0.5  # 同步请求强制请求间隔
    REQUEST_VERIFY: Union[bool, str] = False


@lru_cache
def get_settings():
    """
    读取配置优化
    :return:
    """
    return Settings()


settings = get_settings()

__all__ = ['settings']
