# -*- coding: utf-8 -*-
'''
@author: liww
@file: templates.py
@time: 2020/12/4 11:20
@desc:
'''
from src.deploy import deploy
from flask import request

from src.deploy.zabbix.auxiliary import ZabbixCollect
from src.general.General import Result


@deploy.route('/deploy/zabbix/templates', methods=['GET', 'POST', 'PUT', 'DELETE'])
def zabbix_templates():
    if request.method == 'GET':
        z_c = ZabbixCollect()
        info = z_c.get_template()

        return Result.success_response(data=info)
