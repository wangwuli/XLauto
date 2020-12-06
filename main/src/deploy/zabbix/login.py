# -*- coding: utf-8 -*-
'''
@author: liww
@file: login.py
@time: 2020/11/20 17:41
@desc:
'''
import logging

from flask import current_app
from main.src.setting.auxiliary import query_portal_label_info, alone_query_portal_label_info
from pyzabbix import ZabbixAPI


def zabbix_api_login(zabbix_server_info=None, xlauto=None):

    if not zabbix_server_info:
        zabbix_server_info = query_portal_label_info("zabbix")

    zabbix_server = zabbix_server_info["portal_url"]
    zabbix_user = zabbix_server_info["portal_login_user"]
    zabbix_password = zabbix_server_info["portal_login_pwd"]

    try:
        zapi = ZabbixAPI(zabbix_server)
        zapi.login(zabbix_user, zabbix_password)
        if xlauto:
            xlauto.logger.info('Zabbix登陆成功')
        else:
            current_app.logger.info('Zabbix登陆成功')
        return zapi
    except Exception as e:
        if xlauto:
            xlauto.logger.warning('Zabbix登陆失败：%s' % e)
        else:
            current_app.logger.warning('Zabbix登陆失败：%s' % e)
        return [False, e]


def zabbix_setting_control(xlauto):

    zabbix_label_info = alone_query_portal_label_info('zabbix')

    if zabbix_label_info['portal_disabled'] != 1:

        zabbix_api = zabbix_api_login(zabbix_label_info, xlauto)

        xlauto.config.xlautoenv['zabbix_api'] = zabbix_api
        return True
    else:
        xlauto.config.xlautoenv['zabbix_api'] = ''
        return False
