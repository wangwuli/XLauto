# -*- coding: utf-8 -*-
'''
@author: liww
@file: dao.py
@time: 2020/12/23 15:58
@desc:
'''
from flask import current_app

from models.models import SoftwareConfParameter, db
from src.general.Sqla import Sqla


def save_software_conf_parameter(data_dict, no_continuous=True):
    package_obj = SoftwareConfParameter(software_conf_id=data_dict['software_conf_id'],
                               replacement_entry=data_dict['replacement_entry'],
                               replacement_value=data_dict['replacement_value'],
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


def get_software_conf_parameter(software_conf_id):
    sql = """
        SELECT * FROM software_conf_parameter a
        WHERE a.software_conf_id = :software_conf_id
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, {"software_conf_id": software_conf_id})

    return data