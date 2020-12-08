# -*- coding: utf-8 -*-
'''
@author: liww
@file: dao.py
@time: 2020/12/7 17:05
@desc:
'''
from flask import current_app

from main.models.models import ZabbixAgent, db
from src.general.Sqla import Sqla
from src.general.Transform import model_to_dict


def get_zabbix_agent_info(host_ids):
    # zabbix_agent_info = db.session.query(ZabbixAgent.zabbix_install_id, ZabbixAgent.host_id,
    #                                      ZabbixAgent.zabbix_host_name, ZabbixAgent.install_info, ZabbixAgent.execute_result,
    #                                      ZabbixAgent.zabbix_hostid, ZabbixAgent.zabbix_groupids,
    #                                      ZabbixAgent.zabbix_templateids, ZabbixAgent.monitored_by_proxy_id).filter(
    #     ZabbixAgent.host_id.in_(host_ids)).all()
    # db.session.close()
    # db.session.remove()
    sql = """
    SELECT a.*,b.host_ip,b.host_name FROM zabbix_agent a
    LEFT JOIN host_instance b ON a.host_id = b.host_id
    WHERE a.host_id IN :host_ids
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, {'host_ids': host_ids})

    return data