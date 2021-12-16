#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import xlrd

from src.common.log import log
from src.core.path_settings import XLSX_FILE

'''
xlrd 最新版不再支持 xlsx 文件，只支持 xls,如果使用xlrd, 则需要使用旧版本 1.2.0
解决办法：
1，使用 xls 文件
2，使用 xlrd == 1.2.0

此框架内使用 解决方法2
'''


class ReadExcel:
	"""读取excel文件数据"""

	def __init__(self, fileName, SheetName="Sheet1"):
		"""
		:param fileName: 文件名
		:param SheetName: 文件标签页
		"""
		file = os.path.join(XLSX_FILE, fileName)
		self.data = xlrd.open_workbook(file)
		self.table = self.data.sheet_by_name(SheetName)
		# 获取总行数、总列数
		self.rows = self.table.nrows
		self.cols = self.table.ncols

	def read_data(self):
		"""
		:return: 文件数据
		"""
		if self.rows > 1:
			# 获取第一行的内容，列表格式
			keys = self.table.row_values(0)
			data_list = []
			# 获取每一行的内容，列表格式
			for col in range(1, self.rows):
				values = self.table.row_values(col)
				# keys，values组合转换为字典
				api_dict = dict(zip(keys, values))
				data_list.append(api_dict)
			return data_list
		else:
			log.warning("数据表格没有数据!")
			return None
