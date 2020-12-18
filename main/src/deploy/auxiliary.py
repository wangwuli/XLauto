# -*- coding: utf-8 -*-
'''
@author: liww
@file: auxiliary.py
@time: 2020/12/16 12:29
@desc:
'''
from jinja2 import Template

def replace_text_parameter(text, parameter):
    """
    替换文本参数，用于替换配置与系统执行命令
    :param text:
    :param parameter: diet{'需替换参数名': 参数}
    by: Template('find {{ directory }}').render({'directory': '1'})
    :return:
    """
    return Template(text).render(parameter)
    
