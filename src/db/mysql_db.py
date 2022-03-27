#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
from dbutils.pooled_db import PooledDB

from src.common.log import log
from src.core.conf import settings


class DB:

    def __init__(self):
        try:
            self.conn = PooledDB(
                pymysql,
                maxconnections=15,
                blocking=True,  # 防止连接过多报错
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                database=settings.DB_DATABASE,
                charset=settings.DB_CHARSET,
            ).connection()
        except BaseException as e:
            log.error(f'数据库连接失败 \n {e}')
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        """
        数据库操作执行
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            log.error(f'执行 {sql} 失败 \n {e}')
        else:
            self.close()

    def close(self):
        """
        关闭数据库
        :return:
        """
        self.cursor.close()
        self.conn.close()


db = DB()
