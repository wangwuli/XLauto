# -*- coding: utf-8 -*-
'''
@author: liww
@file: dao.py
@time: 2020/12/7 17:05
@desc:
'''
from flask import current_app

from main.models.models import ZabbixAgent, db, HostInstance
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
    SELECT a.*,b.host_ip,b.host_name,c.project_code FROM zabbix_agent a
    LEFT JOIN host_instance b ON a.host_id = b.host_id
    LEFT JOIN projects c ON  b.host_project = c.project_id
    WHERE a.host_id IN :host_ids
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, {'host_ids': host_ids})

    return data


def get_host_info(host_ids):
    sql = """
    SELECT a.host_id,a.host_ip,b.project_code 
    FROM host_instance a
    LEFT JOIN projects b ON  a.host_project = b.project_id 
    WHERE a.host_id IN :host_ids
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, {'host_ids': host_ids})
    return data



def delete_zabbix_agent(host_ids):
    delete_zabbix_agent_obj = ZabbixAgent.query.filter(ZabbixAgent.host_id.in_(host_ids)).all()

    for delete_zabbix_agent_obj_one in delete_zabbix_agent_obj:
        db.session.delete(delete_zabbix_agent_obj_one)

    db.session.commit()
    db.session.close()
    db.session.remove()
    return True


def update_zabbix_agent(zabbix_info_host, host_info):

    for zabbix_info_host_one in zabbix_info_host:
        for host_info_one in host_info:
            if zabbix_info_host_one['host'] == host_info_one['zabbix_host_name']:
                zabbix_obj = ZabbixAgent(zabbix_hostid=zabbix_info_host_one["hostid"],
                                        zabbix_host_name=zabbix_info_host_one["host"],
                                        zabbix_groupids=[i['groupid'] for i in zabbix_info_host_one["groups"]],
                                        zabbix_templateids=[i['templateid'] for i in
                                                            zabbix_info_host_one["parentTemplates"]],
                                        monitored_by_proxy_id=zabbix_info_host_one["proxy_hostid"],
                                        host_id=host_info_one['host_id'],
                                        )
                db.session.add(zabbix_obj)
    db.session.commit()
    db.session.close()
    db.session.remove()

    return True




