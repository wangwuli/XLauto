# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/12/23 15:47
@desc:
'''
import os
from src.dao.zip_method import unzip_distinguish
from src.deploy import deploy
from flask import request, current_app

from src.deploy.soft_package.dao import save_software_package, get_software_package, del_software_package
from src.general.General import Result, ReturnG
import shutil


@deploy.route('/deploy/soft_package', methods=['GET', 'POST', 'PUT', 'DELETE'])
def soft_package():
    if request.method == 'GET':
        data = request.args
        return_data = get_software_package()
        return Result.success_response(data=return_data, msg='上传成功')

    elif request.method == 'POST':
        f_obj = request.files['file']

        data_dict = request.form.to_dict()

        current_app_ = current_app
        soft_path = os.path.join(current_app_.config.xlautoenv['PROJECT_PATH'], current_app_.config['PACKAGE'],
                                 'software',
                                 data_dict['software_name'], data_dict['software_versions'])
        if not os.path.exists(soft_path):
            os.makedirs(soft_path)
        script_path_file = os.path.join(soft_path, f_obj.filename)
        f_obj.save(script_path_file)

        data_dict['package_path'] = soft_path

        # 解压包文件
        unzip_info = unzip_distinguish(data_dict['software_package_zipanalysis_type'], script_path_file, soft_path)
        if not ReturnG.if_ft(unzip_info):
            Result.fail_response(msg=unzip_info[1])

        # 包信息入库
        save_software_package(data_dict)

        return Result.success_response(msg='上传成功')

    elif request.method == 'DELETE':
        data_dict = request.get_json()
        software_package_info = data_dict['software_package_info']

        del_list = []
        path_list = []
        for software_package_info_one in software_package_info:
            del_list.append(software_package_info_one['software_package_id'])

            if os.path.isdir(software_package_info_one['package_path']):
                path_list.append(software_package_info_one['package_path'])

        for path_list_one in path_list:
            shutil.rmtree(path_list_one)
        del_software_package(del_list)

        return Result.success_response(msg='删除成功')