#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pymysql import connect
from pymysql.err import OperationalError

from src.core.path_settings import DB_CHARSET, DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
from src.common.log import log


class DB:

    def __init__(self):
        try:
            self.conn = connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE,
                                charset=DB_CHARSET)
        except OperationalError as e:
            log.error('数据库连接失败\n', e)
        self.cursor = self.conn.cursor()

    def insert(self, table_name, table_data):
        """
        插入表数据
        :param table_name: 表名
        :param table_data: 表数据
        :return:
        """
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        self.cursor.execute(real_sql)
        self.conn.commit()

    def clear(self, table_name):
        """
        清除表数据
        :param table_name: 表名
        :return:
        """
        real_sql = "delete from " + table_name + ";"
        # 取消表的外键约束
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        self.cursor.execute(real_sql)
        self.conn.commit()

    def close(self):
        """
        关闭数据库
        :return:
        """
        self.conn.close()

    def init_data(self, data):
        """
        初始化数据
        :param data: 表数据
        :return:
        """
        for table, data in data.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()
