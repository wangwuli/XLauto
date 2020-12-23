# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/12/23 15:47
@desc:
'''
import os
import uuid

from src.deploy import deploy
from flask import request, current_app
from src.general.General import Result


@deploy.route('/deploy/soft_package', methods=['GET', 'POST', 'PUT', 'DELETE'])
def soft_package():
    if request.method == 'POST':
        f_obj = request.files['file']

        data_dict = request.form

        current_app_ = current_app
        soft_path = os.path.join(current_app_.config.xlautoenv['PROJECT_PATH'], current_app_.config['PACKAGE'],
                                   data_dict['software_name'])
        if not os.path.exists(soft_path):
            os.makedirs(soft_path)
        script_path_file = os.path.join(soft_path, str(uuid.uuid1()))
        f_obj.save(script_path_file)

        return Result.success_response(msg='上传成功')
