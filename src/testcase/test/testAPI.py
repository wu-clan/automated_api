#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import unittest

import ddt

from src.common.excel_report import WriteExcel
from src.common.log import log
from src.common.read_excel import ReadExcel
from src.common.read_yaml import ReadYaml
from src.common.send_requests import SendRequests
from src.common.yaml_report import WriteYaml
from src.core.path_settings import YAML_FILE

testData = ReadExcel('DemoAPITestCase.xlsx').read_data()
yamlData = ReadYaml().read_yaml('DemoAPITestCase.yaml')
yamlFile = os.path.join(YAML_FILE, 'DemoAPITestCase.yaml')


@ddt.ddt
class Demo_API(unittest.TestCase):
	"""
	三种方式编写用例参数
	1，excel 获取数据
	2, yaml1 先解析文件，后获取数据
	3, yaml2 利用 ddt.file_data() 直接解析获取数据
	"""

	@ddt.data(*testData)
	def test_api1(self, data):
		rowNum = int(data['ID'].split("_")[2])
		log.info(f"---------- 正在执行用例 -> {data['ID']} ----------")
		log.info(f"请求方式: {data['method']}，请求URL: {data['url']}")
		log.info(f"请求参数: {data['params']}")
		log.info(f"请求body类型为：{data['type']} ,body内容为：{data['body']}")
		# 发送请求
		re = SendRequests().send_requests_by_excel(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("页面返回信息：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"用例测试结果:  {data['ID']} ----> {status}")
			WriteExcel().write_data(rowNum + 1, status)
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"用例测试结果:  {data['ID']} ----> {status}")
			WriteExcel().write_data(rowNum + 1, status)
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)

	@ddt.data(*yamlData)
	def test_api2(self, data):
		log.info(f"---------- 正在执行用例 -> {data['ID']} ----------")
		log.info(f"请求方式: {data['method']}，请求URL: {data['url']}")
		log.info(f"请求参数: {data['params']}")
		log.info(f"请求body类型为：{data['type']} ,body内容为：{data['body']}")
		# 发送请求
		re = SendRequests().send_requests_by_yaml(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("页面返回信息：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"用例测试结果:  {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data={'-': {'data': {'request': data, 'response': result}}})
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"用例测试结果:  {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data={'-': {'data': {'request': data, 'response': result}}})
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)

	@ddt.file_data(yamlFile)
	def test_api3(self, **data):
		log.info(f"---------- 正在执行用例 -> {data['ID']} ----------")
		log.info(f"请求方式: {data['method']}，请求URL: {data['url']}")
		log.info(f"请求参数: {data['params']}")
		log.info(f"请求body类型为：{data['type']} ,body内容为：{data['body']}")
		# 发送请求
		re = SendRequests().send_requests_by_yaml(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("页面返回信息：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"用例测试结果:  {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data={'-': {'data': {'request': data, 'response': result}}})
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"用例测试结果:  {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data={'-': {'data': {'request': data, 'response': result}}})
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)


