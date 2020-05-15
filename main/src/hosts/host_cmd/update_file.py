# -*- coding: utf-8 -*-
'''
@author: liww
@file: update_file.py
@time: 2020/5/15 14:41
@desc:
'''
import os
import uuid

from flask import request, current_app

from src.general.General import Result
from src.hosts import hosts
from werkzeug.utils import secure_filename

@hosts.route('/hosts/update_script_file', methods=['POST','GET'])
def update_script_file():
    f_obj = request.files['file']
    current_app_ = current_app
    script_path = os.path.join(current_app_.config.xlautoenv['PROJECT_PATH'], current_app_.config['DATA_PATH'], 'scriptfiles')
    if not os.path.exists(script_path):
        os.makedirs(script_path)

    script_path_file = os.path.join(script_path, secure_filename(f_obj.filename))
    if os.path.exists(script_path_file):
        script_path_file += '_%s'%str(uuid.uuid1())
    f_obj.save(script_path_file)
    return Result.success_response(msg='上传成功')