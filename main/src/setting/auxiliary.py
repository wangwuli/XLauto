# -*- coding: utf-8 -*-
'''
@author: liww
@file: auxiliary.py
@time: 2020/11/18 11:56
@desc:
'''
import os
import time
import paramiko
import threading
from src.general.Connect_G import SCPMet
from src.general.Transform import model_to_dict
from main.models.models import SystemOtherPortal, db


def query_portal_label_info(portal_label):
    """
    配置内容查询
    :param portal_label:
    :return:
    """
    sys_code_data = db.session.query(SystemOtherPortal.system_other_portals_id, SystemOtherPortal.portal_name,
                                     SystemOtherPortal.portal_url, SystemOtherPortal.portal_login_user, SystemOtherPortal.portal_login_pwd).filter(
        SystemOtherPortal.portal_label == portal_label).all()
    db.session.close()
    db.session.remove()
    data = model_to_dict(sys_code_data)

    return data


def save_portal_label_zabbix_info(data_dict):
    """
    保存Zabbix信息
    :param data_dict:
    :return:
    """
    portal_label_infot_obj = SystemOtherPortal.query.filter_by(system_other_portals_id=data_dict['system_other_portals_id']).first()
    portal_label_infot_obj.portal_url = data_dict['portal_url']
    portal_label_infot_obj.portal_login_user = data_dict['portal_login_user']
    portal_label_infot_obj.portal_login_pwd = data_dict['portal_login_pwd']

    db.session.commit()
    db.session.close()
    db.session.remove()

    return True