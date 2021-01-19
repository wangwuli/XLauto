# -*- coding: utf-8 -*-
'''
@author: liww
@file: dao.py
@time: 2020/12/23 15:58
@desc:
'''
from flask import current_app

from models.models import SoftwarePackage, db
from src.general.Sqla import Sqla


def save_software_package(data_dict):
    package_obj = SoftwarePackage(software_name=data_dict['software_name'],
                                  software_versions=data_dict['software_versions'],
                                  package_path=data_dict['package_path'],
                                  software_package_zip_type=data_dict['software_package_zip_type'],
                                  package_storage_type=data_dict['package_storage_type'])

    db.session.add(package_obj)
    db.session.commit()
    db.session.close()
    db.session.remove()

    return True


def get_software_package():
    sql = """
        SELECT a.`*`,b.code_name AS software_package_zip_type_name,c.code_name AS package_storage_type_name
        FROM software_package a
        LEFT JOIN sys_code b ON a.software_package_zip_type = b.code_key AND b.code_type = "software_package_zip_type"
        LEFT JOIN sys_code c ON a.package_storage_type = c.code_key AND c.code_type = "package_storage_type"
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql)

    return data

def get_software_package_one(software_package_id):
    sql = """
        SELECT *
        FROM software_package a
        WHERE a.software_package_id = :software_package_id
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql,{'software_package_id': software_package_id}, fecth='one')

    return data