# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/6/24 16:43
@desc:
'''

from flask import request
from src.general.General import Result
from src.setting.auxiliary import query_portal_label_info, save_portal_label_info, zabbix_setting_control
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
        zabbix_setting_control_status = zabbix_setting_control()

        if zabbix_setting_control_status != True:
            Result.fail_response(msg="保存失败：%s" %zabbix_setting_control_status[1])

        save_portal_label_info(data_dict_form)
        return Result.success_response(msg='保存成功')

