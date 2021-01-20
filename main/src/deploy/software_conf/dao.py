# -*- coding: utf-8 -*-
'''
@author: liww
@file: dao.py
@time: 2020/12/23 15:58
@desc:
'''
from flask import current_app

from models.models import SoftwareConf, db
from src.general.Sqla import Sqla


def save_software_conf(data_dict, no_continuous=True):
    package_obj = SoftwareConf(software_conf_name=data_dict['file_name'],
                               software_package_id=data_dict['software_package_id'],
                               software_conf_path=data_dict['file_path'],
                               software_conf_type=data_dict.get('software_conf_type'),
                               comment=data_dict.get('comment')
                               )
    db.session.add(package_obj)
    db.session.commit()
    db.session.close()
    if no_continuous:
        db.session.remove()
    else:
        return db
    return True


def get_software_conf(software_package_id):
    sql = """
        SELECT a.`*`,b.code_name AS software_conf_type_name
        FROM software_conf a
        LEFT JOIN sys_code b ON a.software_conf_type = b.code_key AND b.code_type = "software_conf_type"
        WHERE a.software_package_id = :software_package_id
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, {"software_package_id": software_package_id})

    return data