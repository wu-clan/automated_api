#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import ddt

from src.common.excel_report import WriteExcel
from src.common.log import log
from src.common.myunit import Unit
from src.common.read_excel import ReadExcel
from src.common.read_yaml import ReadYaml
from src.common.send_requests import sync_request, sync_httpx
from src.common.yaml_report import WriteYaml
from src.utils.get_yaml_file import get_yaml
from src.utils.log_current_req import log_current_req_data

testData = ReadExcel('DemoAPITestCase.xlsx').read_data()
yamlData = ReadYaml('DemoAPITestCase.yaml').read_yaml()
yamlFile = get_yaml('DemoAPITestCase.yaml')


@ddt.ddt
class Demo_API(Unit):
	"""
	三种方式编写用例参数
	1，excel 获取数据
	2, yaml1 先解析文件，后获取数据
	3, yaml2 利用 ddt.file_data() 直接解析获取数据
	"""

	@ddt.data(*testData)
	def test_api1(self, data):
		row_num = int(data['ID'].split("_")[2]) + 1
		log_current_req_data(data)
		# 发送请求
		re = sync_request(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("response：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"test result: {data['ID']} ----> {status}")
			WriteExcel().write_data(row_num, status)
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"test result: {data['ID']} ----> {status}")
			WriteExcel().write_data(row_num, status)
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)

	@ddt.data(*testData)
	def test_api2(self, data):
		row_num = int(data['ID'].split("_")[2]) + 1
		log_current_req_data(data)
		# 发送请求
		re = sync_httpx(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("response：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"test result: {data['ID']} ----> {status}")
			WriteExcel().write_data(row_num, status)
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"test result: {data['ID']} ----> {status}")
			WriteExcel().write_data(row_num, status)
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)

	@ddt.data(*yamlData)
	def test_api3(self, data):
		log_current_req_data(data)
		# 发送请求
		re = sync_request(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("response：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"test result: {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data=[{f"{None}": {'request': data, 'response': result}}])
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"test result: {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data=[{f"{None}": {'request': data, 'response': result}}])
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)

	@ddt.file_data(yamlFile)
	def test_api4(self, **data):
		log_current_req_data(data)
		# 发送请求
		re = sync_httpx(data)
		# 获取服务端返回的值
		result = re.json()
		code = int(result['code'])
		msg = str(result['msg'])
		log.info("response：%s" % re.content.decode("utf-8"))
		# 获取excel表格数据的状态码和消息
		read_code = int(data["status_code"])
		read_msg = data["msg"]
		if read_code == code and read_msg == msg:
			status = 'PASS'
			log.success(f"test result: {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data=[{f"{None}": {'request': data, 'response': result}}])
		if read_code != code or read_msg != msg:
			status = 'FAIL'
			log.error(f"test result: {data['ID']} ----> {status}")
			WriteYaml().write_yaml(data=[{f"{None}": {'request': data, 'response': result}}])
		self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
		self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)


