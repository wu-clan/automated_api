#!/usr/bin/env python
# -*- coding: utf-8 -*-


from conf.settings import PATTERN
from lib.global_variables import gv

import re
def parameter_substitution(strParam):
    '''依赖参数值替换为实际值'''
    keys = re.findall(PATTERN, strParam)
    for key in keys:
        value = gv.getVar(key)
        strParam = strParam.replace('${' + key + '}', str(value))  # replace返回替换后的新字符串
    return strParam
