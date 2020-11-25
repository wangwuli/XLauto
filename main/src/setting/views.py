# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/6/24 16:43
@desc:
'''

from flask import request
from flask import current_app
from src.deploy.zabbix.login import zabbix_api_login
from src.general.General import Result
from src.setting.auxiliary import query_portal_label_info, save_portal_label_info
from . import setting


@setting.route('/setting/main', methods=['GET','POST'])
def setting_main():
    if request.method == 'GET':
        data = request.args
        data = query_portal_label_info(data['portal_label'])
        return Result.success_response(data=data, msg='查询成功')
    elif request.method == 'POST':
        data_dict = request.get_json()
        save_portal_label_info(data_dict['form'])
        return Result.success_response(msg='保存成功')


@setting.route('/setting/main/zabbix', methods=['POST'])
def setting_main_zabbix():
    if request.method == 'POST':
        data_dict = request.get_json()

        data_dict_form = data_dict['form']
        if data_dict_form['portal_disabled']:
            zabbix_str = zabbix_api_login()
            if zabbix_str[0]:
                current_app.config.xlautoenv['zabbix_key'] = zabbix_str
            else:
                Result.fail_response(msg="保存失败：%s" %zabbix_str[1])
        else:
            current_app.config.xlautoenv['zabbix_key'] = ''

        save_portal_label_info(data_dict_form)
        return Result.success_response(msg='保存成功')

