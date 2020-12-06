# -*- coding: utf-8 -*-
'''
@author: liww
@file: startup.py
@time: 2020/11/26 17:23
@desc:
'''
import os

from src.deploy.zabbix.login import zabbix_setting_control
import settings

def setting_control(xlauto):
    #zabbix功能配置
    zabbix_setting_control(xlauto)
