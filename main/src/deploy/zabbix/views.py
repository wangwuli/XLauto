# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/11/20 17:26
@desc:
'''

from src.deploy import deploy
from src.deploy.zabbix.dao import get_zabbix_agent_info
from src.general.General import Result
from flask import request, current_app


@deploy.route('/deploy/zabbix/agents_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def zabbix_agents_install():
    if request.method == 'GET':
        """
        获取已存Zabbix信息
        """
        data = request.args
        host_ids_list  = data['host_ids'].split(",")

        zabbix_agent_info = get_zabbix_agent_info(host_ids_list)

        return Result.success_response(data=zabbix_agent_info, msg="查询成功")



    if request.method == 'POST':
        data = request.get_json()

        return Result.success_response(msg="修改")