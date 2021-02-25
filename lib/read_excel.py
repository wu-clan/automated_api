#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import os, sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from conf.settings import DATA_PATH

file_path = DATA_PATH + '/testcase.xlsx'

# print(file_path)

def read_excel(sheet_name="Sheet1", excel_path=file_path):
    # 打开文件
    workbook = xlrd.open_workbook(excel_path)

    # 获取所有sheet
    # sheets = workbook.sheet_names()
    # print(sheets) # ['Sheet1', 'Sheet2', 'Sheet3']

    # 根据sheet名称获取sheet内容(也可以格局索引，从0开始)
    sheet = workbook.sheet_by_name(sheet_name)

    # 获取第二行作为key
    first_row = sheet.row_values(1)

    # 获取行数
    rows_length = sheet.nrows

    all_rows = []
    rows_dict = []
    for i in range(rows_length):
        if i<2:
            continue
        all_rows.append(sheet.row_values(i))
    for row in all_rows:
        lis = dict(zip(first_row,row))
        rows_dict.append(lis)
    return rows_dict




if __name__ == '__main__':
    res = read_excel()
    print(res)


