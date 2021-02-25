#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import inspect

class GetCurrentItems(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance 
    def __init__(self):
        pass

    @staticmethod
    def get_current_file_path():
        return __file__

    def get_current_class_name(self):
        return self.__class__.__name__

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    @staticmethod
    def get_current_lineno():
        return sys._getframe().f_lineno


p = GetCurrentItems()    



    




