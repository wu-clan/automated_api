#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记



import unittest
from lib.global_variables import gv
from lib.parameter_substitution import parameter_substitution
from ddt import *
import requests, time
from lib.read_excel import read_excel
from lib.assert_res import assert_res
from conf.settings import SHEET_NAME
from lib.logger import logger

@ddt
class MyRequest(unittest.TestCase):
    test_datas = read_excel(SHEET_NAME)

    @data(*test_datas)
    @unpack
    # def test_my_request_(self, url, method, headers, cookies, params, body, globalVariable, assertRes, init_sql):
    def test_my_request_(self, project, module, case_id, case_name, description, url, method, headers, cookies, params, body, file, init_sql, globalVariable, assertRes, request, actualResults, result, tester):
        '''请求'''
        logger.logger.debug("==========【当前执行用例是：%s：%s】==========" % (case_id, case_name))
        # 可能参数化的地方是url，headers，cookies, params, body
        url = parameter_substitution(url)
        headers = parameter_substitution(headers)
        cookies = parameter_substitution(cookies)
        params = parameter_substitution(params)
        body = parameter_substitution(body)
        logger.logger.debug("> > > > >请求的method是：%s" % method)
        logger.logger.debug("> > > > >请求的url是：%s" % url)
        logger.logger.debug("> > > > >请求的headers是：%s" % headers)
        logger.logger.debug("> > > > >请求的cookies是：%s" % cookies)
        logger.logger.debug("> > > > >请求的params是：%s" % params)
        logger.logger.debug("> > > > >请求的body是：%s" % body)
        logger.logger.debug("> > > > >断言内容assertRes是：%s" % assertRes)

        # 转换
        headers_ = eval(headers) if headers else headers
        cookies_ = eval(cookies) if cookies else cookies
        params_ = eval(params) if params else params
        body_ = eval(body) if body else body

        if init_sql:
            pass
            
        time.sleep(5)
        # get请参考post完善
        if method.upper() == 'GET':
            try:
                requests.DEFAULT_RETRIES = 5
                s = requests.session()
                s.keep_alive = False
                
                res = requests.get(url=url,headers=headers_, cookies=cookies_, params=params_,timeout=10)
                logger.logger.debug("执行请求后，结果是：%s"%res.text)
                # 如果有需要被后续请求用的变量数据
                if globalVariable:
                    gv.save_global_variable(globalVariable,res.text)

                # 断言
                if assertRes:
                    res_status = assert_res(assertRes, res.text)
                    logger.logger.debug("断言结果是：%s\n\n" % res_status)
                    gv.res.append([res.text,url,headers,cookies,params,body,res_status])
                    self.assertEqual(res_status, "pass")
            except Exception as e:
                print('出错了，错误是%s' % e)
                raise e


        elif method.upper() == 'POST':
            # 执行请求
            try:
                res = requests.post(url=url,headers=headers_, cookies=cookies_, params=params_, json=body_, timeout=10)
                logger.logger.debug("执行请求后，结果是：%s"%res.text)
                # print("执行请求后，结果是： ")
                # 如果有需要被后续请求用的变量数据
                if globalVariable:
                    gv.save_global_variable(globalVariable,res.text)

                # 断言
                if assertRes:
                    res_status = assert_res(assertRes, res.text)
                    logger.logger.debug("断言结果是：%s\n\n" % res_status)
                    gv.res.append([res.text,url,headers,cookies,params,body,res_status])
                    self.assertEqual(res_status, "pass")


            except Exception as e:
                print('出错了，错误是%s' % e)
                raise e


if __name__ =='__main__':
    pass