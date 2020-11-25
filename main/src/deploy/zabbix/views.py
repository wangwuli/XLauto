# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/11/20 17:26
@desc:
'''

from src.dao import hosts
from src.dao.hosts_operation import host_action_execute
from src.deploy import deploy
from src.general.General import ReturnG, Result
from flask import request, current_app
from src.general.Sqla import Sqla



@deploy.route('/deploy/zabbix/agents_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def zabbix_agents_install():
    if request.method == 'GET':
        """
        获取信息
        """
        data = request.args

    if request.method == 'POST':
        data = request.get_json()

        return Result.success_response(msg="修改")