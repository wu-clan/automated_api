#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:59
# @Blog    : http://www.cnblogs.com/uncleyong
# @Gitee   : https://gitee.com/uncleyong
# @QQ交流群 : 652122175
# @公众号   : 全栈测试笔记

# class GlobalVariables(object):
#     def __init__(self):
#         self.gv = {}
#
# if __name__ == '__main__':
#     a = GlobalVariables()
#     print(a.gv)

import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)
from conf.settings import PROJECT_IP

import json



class GlobalVariables(object):
    '''单例对象，保存依赖数据'''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        self.globalVars = {"ip": PROJECT_IP}
        self.res = []

    def setVar(self,key,value):
        '''添加全局变量'''
        self.globalVars[key] = value
        print("当前全局变量：",self.globalVars)

    def getVar(self,key):
        '''获取某个全局变量'''
        return self.globalVars.get(key)

    def getVars(self):
        '''获取全部全局变量'''
        return self.globalVars

    def deleteVar(self,key):
        '''删除某个全局变量'''
        self.globalVars.pop(key)

    def cleanVars(self):
        '''清空全局变量'''
        self.globalVars.clear()

    def deleteVars(self):
        '''删除全局变量'''
        del self.globalVars

    def save_global_variable(self, globalVariable, res):
        '''保存被依赖数据到全局变量中'''
        import jsonpath
        for globalv in globalVariable.split(";"):
            g = globalv.strip()
            if g:
                key = g.split('=')[0].strip()
                value_expr = g.split('=')[1].strip()
                print("key:", key)
                print("value_expr:", value_expr)
                value = jsonpath.jsonpath(json.loads(res),value_expr)[0]  # 返回列表，取第一个

                self.setVar(key,value)
        self.getVars()  # 打印当前所有全局变量

gv = GlobalVariables()

# print(gv.globalVars)
if __name__ == '__main__':
    pass