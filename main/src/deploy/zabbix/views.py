# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/11/20 17:26
@desc:
'''

from src.deploy import deploy
from src.deploy.zabbix.auxiliary import ZabbixCollect
from src.deploy.zabbix.dao import get_zabbix_agent_info, get_host_info, update_zabbix_agent, delete_zabbix_agent
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
        """
        同步Zabbix信息
        """
        data = request.get_json()
        host_info = get_host_info(data['host_ids'])

        conjecture_zabbix_host_name_list = []
        for host_info_one in host_info:
            conjecture_zabbix_host_name = "%s.%s" % (host_info_one['host_ip'], host_info_one['project_code'])
            conjecture_zabbix_host_name_list.append(conjecture_zabbix_host_name)
            host_info_one['zabbix_host_name'] = conjecture_zabbix_host_name

        #向zabbix请求同步数据
        z_c = ZabbixCollect()
        zabbix_info_host = z_c.get_host(conjecture_zabbix_host_name_list)

        #新建同步数据，清理已经不存在的数据
        delete_zabbix_agent(data['host_ids'])
        update_zabbix_agent(zabbix_info_host, host_info)

        #查询最新的数据返回前端
        zabbix_agent_info = get_zabbix_agent_info(data['host_ids'])

        return Result.success_response(data=zabbix_agent_info, msg="同步成功")

    if request.method == 'PUT':
        """
        安装并记录Zabbix信息
        """
        data = request.get_json()

        return Result.success_response(data=data, msg="安装成功")
