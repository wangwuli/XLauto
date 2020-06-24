# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/6/24 16:43
@desc:
'''
from flask import request, current_app

from models.models import HostUser
from src.general.General import Result
from src.hosts import hosts


@hosts.route('/hosts/add_host', methods=['POST'])
def update_script_file():
    data_dict = request.get_json()


    #新增主机，如果有主机用户一并新增，注意用户角色假如为空的情况
    # HostUser(host_id=host_id, user_name=user_name)
    # db.session.add(file_sql_obj)
    # db.session.commit()
    # db.session.close()
    # host_project: '',
    # host_type: '',
    # hosts_input_text: '',
    # username: '',
    # password: ''
    # #
    #
    # file_sql_obj = ScriptFileCabinet(script_file_path=script_path_file, script_file_name=f_obj.filename)
    #
    #
    # f_obj.save(script_path_file)

    return Result.success_response(msg='新增成功')