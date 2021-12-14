#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pymysql import connect
from pymysql.err import OperationalError

from src.core.settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
from src.common.log import logger


class DB:

    def __init__(self):
        try:
            self.conn = connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                charset='utf8')
        except OperationalError as e:
            logger.error('数据库连接失败\n', e)
        self.cursor = self.conn.cursor()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        self.cursor.execute(real_sql)
        self.conn.commit()

    # 清除表数据
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        # 取消表的外键约束
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        self.cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()
