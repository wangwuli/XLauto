# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/6/24 16:43
@desc:
'''

from flask import request
from src.general.General import Result
from src.setting.auxiliary import query_portal_label_info, save_portal_label_zabbix_info
from . import setting


@setting.route('/setting/main', methods=['GET','POST'])
def setting_main():
    if request.method == 'GET':
        data = request.args
        data = query_portal_label_info(data['portal_label'])
        return Result.success_response(data=data, msg='查询成功')
    elif request.method == 'POST':
        data_dict = request.get_json()
        save_portal_label_zabbix_info(data_dict['form'])
        return Result.success_response(msg='保存成功')

