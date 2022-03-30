#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import ddt

from src.common.excel_operate import read_excel, write_excel
from src.common.log import log
from src.common.myunit import Unit, AsyncUnit
from src.common.send_requests import send_request
from src.common.yaml_operate import read_yaml, write_yaml, get_yaml

testData = read_excel('DemoAPITestCase.xlsx')
yamlData = read_yaml('DemoAPITestCase.yaml')
yamlFile = get_yaml('DemoAPITestCase.yaml')


@ddt.ddt
class Demo_API(Unit):
    """
    三种方式编写用例参数
    1，excel 获取数据
    2, yaml1 先解析文件，后获取数据, ddt用法同excel
    3, yaml2 利用 ddt.file_data() 直接解析获取数据
    """

    @ddt.data(*testData)
    def test_api1(self, data):
        row_num = int(data['ID'].split("_")[2]) + 1
        # 发送请求
        req = send_request.sync_request(data)
        # 获取服务端返回的值
        result = req.json()
        code = int(result['code'])
        msg = str(result['msg'])
        log.info("response：%s" % req.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        read_code = int(data["status_code"])
        read_msg = data["msg"]
        if read_code == code and read_msg == msg:
            status = 'PASS'
            log.success(f"test result: {data['ID']} ----> {status}")
            write_excel(row_num, status)
        if read_code != code or read_msg != msg:
            status = 'FAIL'
            log.error(f"test result: {data['ID']} ----> {status}")
            write_excel(row_num, status)
        self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
        self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)

    @ddt.file_data(yamlFile)
    def test_api2(self, **data):
        # 发送请求
        req = send_request.sync_httpx(data)
        # 获取服务端返回的值
        result = req.json()
        code = int(result['code'])
        msg = str(result['msg'])
        log.info("response：%s" % req.content.decode("utf-8"))
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
        self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
        self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)


@ddt.ddt
class Demo_API2(AsyncUnit):

    @ddt.data(*testData)
    async def test_api3(self, data):
        # 发送请求
        req = await send_request.async_httpx(data)
        # 获取服务端返回的值
        result = req.json()
        code = int(result['code'])
        msg = str(result['msg'])
        log.info("response：%s" % req.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        read_code = int(data["status_code"])
        read_msg = data["msg"]
        try:
            self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
            self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)
        except Exception:
            log.error(f"test result: {data['ID']} ----> FAIL")
        else:
            log.success(f"test result: {data['ID']} ----> PASS")

    @ddt.file_data(yamlFile)
    async def test_api4(self, **data):
        # 发送请求
        try:
            for _ in range(3):
                req = await send_request.async_aiohttp(data)
                # 获取服务端返回的值
                result = await req.json()  # 注意这里和 httpx 不同
                code = int(result['code'])
                msg = str(result['msg'])
                log.info("response：%s" % await req.text())
                # 获取excel表格数据的状态码和消息
                read_code = int(data["status_code"])
                read_msg = data["msg"]
                self.assertEqual(code, read_code, "返回实际结果是->: %s" % code)
                self.assertEqual(msg, read_msg, "返回实际结果是->: %s" % msg)
        except Exception:
            log.error(f"test result: {data['ID']} ----> FAIL")
        else:
            log.success(f"test result: {data['ID']} ----> PASS")
