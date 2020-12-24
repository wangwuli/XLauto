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

from src.deploy.soft_package.dao import save_software_package
from src.general.General import Result


@deploy.route('/deploy/soft_package', methods=['GET', 'POST', 'PUT', 'DELETE'])
def soft_package():
    if request.method == 'POST':
        f_obj = request.files['file']

        data_dict = request.form.to_dict()

        current_app_ = current_app
        soft_path = os.path.join(current_app_.config.xlautoenv['PROJECT_PATH'], current_app_.config['PACKAGE'],
                                 'software', data_dict['software_versions'],
                                 data_dict['software_name'])
        if not os.path.exists(soft_path):
            os.makedirs(soft_path)
        script_path_file = os.path.join(soft_path, f_obj.filename)
        f_obj.save(script_path_file)

        data_dict['package_path'] = soft_path

        # 解压包文件
        unzip_distinguish(data_dict['software_package_zip_type'], script_path_file, soft_path)

        # 包信息入库
        save_software_package(data_dict)

        return Result.success_response(msg='上传成功')
