# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: views.py
@time: 2021/1/18 17:24
@desc:
'''

from src.file import file_l
from src.general.General import Result
from flask import request


@file_l.route('/file/local_dir', methods=['GET', 'POST', 'PUT', 'DELETE'])
def software_conf():
    if request.method == 'GET':


        return Result.success_response(data='', msg='查询成功')





    elif request.method == 'POST':
        f_obj = request.files['file']

        data_dict = request.form.to_dict()

        return Result.success_response(msg='保存成功')