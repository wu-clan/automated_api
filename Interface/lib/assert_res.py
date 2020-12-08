#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

import jsonpath,json

def assert_res(assertRes, res):
    res_status = 'pass'
    for i in assertRes.split(";"):
        i_ = i.strip()
        if i_:
            actual_expr = i_.split("=")[0].strip()
            actual = jsonpath.jsonpath(json.loads(res), actual_expr)[0]
            expect = i_.split("=")[1].strip()
            if str(actual) != expect:
                # print(type(actual),type(expect))
                # print("expect: ",expect)
                # print("actual: ",actual)
                res_status = 'fail'
                return res_status
    return res_status