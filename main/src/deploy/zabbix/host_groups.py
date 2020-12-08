# -*- coding: utf-8 -*-
'''
@author: liww
@file: host_groups.py
@time: 2020/12/7 16:16
@desc:
'''

from src.deploy import deploy
from flask import request

from src.deploy.zabbix.auxiliary import ZabbixCollect
from src.general.General import Result


@deploy.route('/deploy/zabbix/host_groups', methods=['GET', 'POST', 'PUT', 'DELETE'])
def zabbix_host_groups():
    if request.method == 'GET':
        z_c = ZabbixCollect()
        info = z_c.get_host_group()

        return Result.success_response(data=info)