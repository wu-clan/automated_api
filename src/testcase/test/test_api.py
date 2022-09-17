#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import asyncer
import ddt

from src.common.excel_handler import read_excel, write_excel
from src.common.log import log
from src.common.myunit import Unit, AsyncUnit
from src.common.send_requests import send_request
from src.common.yaml_handler import read_yaml, write_yaml, get_yaml

excel_data = read_excel('DemoAPITestCase.xlsx')
yaml_data = read_yaml('DemoAPITestCase.yaml')
yaml_file = get_yaml('DemoAPITestCase.yaml')


@ddt.ddt
class DemoAPI(Unit):

    @ddt.data(*excel_data)
    def test_api1(self, data):
        row_num = int(data['ID'].split("_")[2]) + 1
        # 发送请求
        response = send_request.send_sync_request(data)
        # 获取服务端返回的值
        result = response.json()
        code = int(result['code'])
        msg = str(result['msg'])
        # 获取excel表格数据的状态码和消息
        read_code = int(data["status_code"])
        read_msg = data["msg"]
        if read_code == code and read_msg == msg:
            status = 'PASS'
            log.success(f"test result: {data['ID']} ----> {status}")
            write_excel(row_num=row_num, status=status)
        if read_code != code or read_msg != msg:
            status = 'FAIL'
            log.error(f"test result: {data['ID']} ----> {status}")
            write_excel(row_num=row_num, status=status)
        self.assertEqual(code, read_code, f"返回实际结果是->: {code}")
        self.assertEqual(msg, read_msg, f"返回实际结果是->: {code}")

    @ddt.file_data(yaml_file)
    def test_api2(self, **data):
        # 发送请求
        req = send_request.send_sync_request(data, request_engin='httpx')
        # 获取服务端返回的值
        result = req.json()
        code = int(result['code'])
        msg = str(result['msg'])
        # 获取excel表格数据的状态码和消息
        read_code = int(data["status_code"])
        read_msg = data["msg"]
        if read_code == code and read_msg == msg:
            status = 'PASS'
            log.success(f"test result: {data['ID']} ----> {status}")
            write_yaml(data=[{status: {'request': data, 'response': result}}])
        if read_code != code or read_msg != msg:
            status = 'FAIL'
            log.error(f"test result: {data['ID']} ----> {status}")
            write_yaml(data=[{status: {'request': data, 'response': result}}])
        self.assertEqual(code, read_code, f"返回实际结果是->: {code}")
        self.assertEqual(msg, read_msg, f"返回实际结果是->: {code}")


@ddt.ddt
class DemoAPI2(AsyncUnit):

    @ddt.data(*yaml_data)
    async def test_api3(self, data):
        row_num = int(data['ID'].split("_")[2]) + 1
        # 发送请求
        response = await send_request.send_async_request(data)
        # 获取服务端返回的值
        result = response.json()
        code = int(result['code'])
        msg = str(result['msg'])
        # 获取excel表格数据的状态码和消息
        read_code = int(data["status_code"])
        read_msg = data["msg"]
        if read_code == code and read_msg == msg:
            status = 'PASS'
            log.success(f"test result: {data['ID']} ----> {status}")
            await asyncer.asyncify(write_excel)(row_num=row_num, status=status)
        if read_code != code or read_msg != msg:
            status = 'FAIL'
            log.error(f"test result: {data['ID']} ----> {status}")
            await asyncer.asyncify(write_excel)(row_num=row_num, status=status)
        self.assertEqual(code, read_code, f"返回实际结果是->: {code}")
        self.assertEqual(msg, read_msg, f"返回实际结果是->: {code}")

    @ddt.file_data(yaml_file)
    async def test_api4(self, **data):
        # 发送请求
        response = await send_request.send_async_request(data, request_engin='aiohttp')
        # 获取服务端返回的值
        result = await response.json()  # 注意这里和 httpx 不同
        code = int(result['code'])
        msg = str(result['msg'])
        # 获取excel表格数据的状态码和消息
        read_code = int(data["status_code"])
        read_msg = data["msg"]
        if read_code == code and read_msg == msg:
            status = 'PASS'
            log.success(f"test result: {data['ID']} ----> {status}")
            await asyncer.asyncify(write_yaml)(data=[{status: {'request': data, 'response': result}}])
        if read_code != code or read_msg != msg:
            status = 'FAIL'
            log.error(f"test result: {data['ID']} ----> {status}")
            await asyncer.asyncify(write_yaml)(data=[{status: {'request': data, 'response': result}}])
        self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
        self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)
        # aiohttp 会触发 RuntimeError: Event loop is closed, 请移步文件 send_request.py 查看说明
