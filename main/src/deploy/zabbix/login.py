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
from src.general.File import str_sin_file


def zabbix_api_login(zabbix_server_info=None,happened_log_path=None):

    if not zabbix_server_info:
        zabbix_server_info = query_portal_label_info("zabbix")

    zabbix_server = zabbix_server_info["portal_url"]
    zabbix_user = zabbix_server_info["portal_login_user"]
    zabbix_password = zabbix_server_info["portal_login_pwd"]

    try:
        zapi = ZabbixAPI(zabbix_server)
        zapi.login(zabbix_user, zabbix_password)
        if happened_log_path:
            logging.info('Zabbix登陆成功')
            # str_sin_file(happened_log_path, 'Zabbix登陆成功')
        else:
            current_app.logger.info('Zabbix登陆成功')
        return zapi
    except Exception as e:
        if happened_log_path:
            logging.info('Zabbix登陆失败：%s' % e)
        else:
            # str_sin_file(happened_log_path, 'Zabbix登陆失败：%s' %e)
            current_app.logger.warning('Zabbix登陆失败：%s' % e)
        return [False, e]


def zabbix_setting_control(happened_log_path):

    zabbix_label_info = alone_query_portal_label_info('zabbix')

    if zabbix_label_info['portal_disabled'] != 1:
        # zabbix_setting_control_status = zabbix_setting_control()
        # if not zabbix_setting_control_status[0]:
        #     return (False, zabbix_setting_control_status[1])

        zabbix_str = zabbix_api_login(zabbix_label_info, happened_log_path)

        current_app.config.xlautoenv['zabbix_key'] = zabbix_str
    else:
        current_app.config.xlautoenv['zabbix_key'] = ''

    return True