# -*- coding: utf-8 -*-
'''
@author: liww
@file: login.py
@time: 2020/11/20 17:41
@desc:
'''
from flask import current_app
from main.src.setting.auxiliary import query_portal_label_info
from pyzabbix import ZabbixAPI

def zabbix_api_login():

    zabbix_server_info = query_portal_label_info("zabbix")

    zabbix_server = zabbix_server_info("portal_url")
    zabbix_user = zabbix_server_info("portal_login_user")
    zabbix_password = zabbix_server_info("portal_login_pwd")

    try:
        zapi = ZabbixAPI(zabbix_server)
        zapi.login(zabbix_user, zabbix_password)
        current_app.logger.info('Zabbix登陆成功')
        return zapi
    except Exception as e:
        current_app.logger.warning('Zabbix登陆失败：%s' %e)
        return [False, e]
