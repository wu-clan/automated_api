#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'xiaowu'

import xlrd

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
		self.data = xlrd.open_workbook(fileName)
		self.table = self.data.sheet_by_name(SheetName)

		# 获取总行数、总列数
		self.nrows = self.table.nrows
		self.ncols = self.table.ncols

	def read_data(self):
		if self.nrows > 1:
			# 获取第一行的内容，列表格式
			keys = self.table.row_values(0)
			listApiData = []
			# 获取每一行的内容，列表格式
			for col in range(1, self.nrows):
				values = self.table.row_values(col)
				# keys，values组合转换为字典
				api_dict = dict(zip(keys, values))
				listApiData.append(api_dict)
			return listApiData
		else:
			print("表格是空数据!")
			return None
