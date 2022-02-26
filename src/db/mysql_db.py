#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
from pymysql.err import OperationalError

from src.common.log import log
from src.core.conf import settings


class DB:

    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                database=settings.DB_DATABASE,
                charset=settings.DB_CHARSET
            )
        except OperationalError as e:
            log.error(f'数据库连接失败\n {e}')
        self.cursor = self.conn.cursor()

    def ect(self, sql):
        """
        数据库操作执行
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            log.error(f'执行 {sql} 时发生错误\n {e}')

    def close(self):
        """
        关闭数据库
        :return:
        """
        self.conn.close()

