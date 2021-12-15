#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json

import requests

from src.common.do_yaml import DoYaml
from src.common.log import log


class SendRequests(object):
	"""发送请求数据"""

	@staticmethod
	def send_requests_by_excel(data):
		"""
		使用excel参数发送请求
		:param data: 请求参数
		:return:
		"""
		try:
			method = data["method"]
			url = data["url"]
			if data["params"] == "":
				params = None
			else:
				params = eval(data["params"])
			if data["headers"] == "":
				headers = None
			else:
				headers = dict(data["headers"])
			if data["body"] == "":
				body_data = None
			else:
				body_data = eval(data["body"])
			if data["type"] == "data":
				body = body_data
			elif data["type"] == "json":
				body = json.dumps(body_data)
			else:
				body = body_data
			# 发送请求
			rq = requests.session().request(method=method, url=url, headers=headers, params=params, data=body, verify=False)
			return rq
		except Exception as e:
			log.error(f'请求发送失败\n{e}')

	@staticmethod
	def send_requests_by_yaml(filename):
		"""
		使用yaml参数发送请求
		:return:
		"""
		try:
			rags = DoYaml().read_yaml(filename)
			method = rags.get('method')
			url = rags.get('url')
			if rags.get("params") == "":
				params = None
			else:
				params = eval(rags.get("params"))
			if rags.get("headers") == "":
				headers = None
			else:
				headers = dict(rags.get("headers"))
			if rags.get("body") == "":
				body_data = None
			else:
				body_data = eval(rags.get("body"))
			if rags.get("type") == "data":
				body = body_data
			elif rags.get("type") == "json":
				body = json.dumps(body_data)
			else:
				body = body_data
			# 发送请求
			rq = requests.session().request(method=method, url=url, headers=headers, params=params, data=body, verify=False)
			return rq
		except Exception as e:
			log.error(f'请求发送失败\n{e}')

