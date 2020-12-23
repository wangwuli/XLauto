# -*- coding: utf-8 -*-
'''
@author: liww
@file: dao.py
@time: 2020/12/23 15:58
@desc:
'''
from models.models import SoftwarePackage, db


def save_software_package(data_dict):
    package_obj = SoftwarePackage(software_name=data_dict['software_name'],
                                  software_versions=data_dict['software_versions'],
                                  package_path=data_dict['package_path'],
                                  software_package_zip_type=data_dict['software_package_zip_type'],
                                  software_install_type=data_dict['software_install_type'])

    db.session.add(package_obj)
    db.session.commit()
    db.session.close()
    db.session.remove()
