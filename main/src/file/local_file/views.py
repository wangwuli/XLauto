# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: views.py
@time: 2021/1/18 17:24
@desc:
'''
from src.deploy.soft_package.dao import get_software_package_one
from src.file import file_l
from src.general.File import get_dir_file
from src.general.General import Result
from flask import request


@file_l.route('/file/local_dir', methods=['GET', 'POST', 'PUT', 'DELETE'])
def software_conf():
    if request.method == 'GET':
        data = request.args
        software_package_id = data['software_package_id']
        soft_obj = get_software_package_one(software_package_id)

        if soft_obj:
            return_data = {'package_path': soft_obj['package_path'].replace('\\', '/') + '/',
                           'package_path_dir_list': get_dir_file(soft_obj['package_path'])
                           }
            return Result.success_response(data=return_data, msg='查询成功')
        else:
            return Result.fail_response(data=[], msg='查询成功')




    elif request.method == 'POST':
        f_obj = request.files['file']

        data_dict = request.form.to_dict()

        return Result.success_response(msg='保存成功')