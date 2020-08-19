# -*- coding: utf-8 -*-
'''
@author: liww
@file: views.py
@time: 2020/6/24 16:43
@desc:
'''
from flask import request, current_app

from models.models import HostUser, HostInstance, db
from src.general.Connect_G import Ip_c
from src.general.General import Result
from src.general.Sqla import Sqla
from src.hosts import hosts


@hosts.route('/hosts/add_host', methods=['POST'])
def hosts_add_host():
    data_dict = request.get_json()

    if not data_dict.get('user_role'):
        user_role = 'root'
    else:
        user_role = data_dict['user_role']

    if not data_dict.get('host_port'):
        host_port = '22'
    else:
        host_port = data_dict['host_port']

    if not data_dict['hosts_input_text'] : return Result.fail_response(msg="不支持的IP输入")

    ip_c = Ip_c()
    ip_list = ip_c.string_formatting(data_dict['hosts_input_text'])
    if not ip_list:
        return Result.fail_response(msg="IP格式异常")

    sqla = Sqla(current_app)

    for ip_one in ip_list:
        host_obj = HostInstance(host_ip=ip_one,
                                host_project=data_dict['host_project'],
                                host_type_key=data_dict['host_type'],
                                host_port=host_port
                                )
        db.session.add(host_obj)
        db.session.flush()
        host_id = host_obj.host_id
        user_pass = sqla.sql_encryption(data_dict['user_pass'])

        user_obj = HostUser(host_id=host_id,
                            user_name=data_dict['user_name'],
                            user_pass=user_pass,
                            user_role=user_role
                            )
        db.session.add(user_obj)
    db.session.commit()
    db.session.close()
    db.session.remove()

    return Result.success_response(msg='新增成功')


@hosts.route('/hosts/del_host', methods=['DELETE'])
def hosts_del_host():
    del_host_info = request.json.get('del_host_info')

    # delete_script_obj = HostInstance.query.filter(HostInstance.host_id.in_(del_host_info)).all()
    # delete_script_obj.is_remove = 1

    db.session.query(HostInstance).filter(HostInstance.host_id.in_(del_host_info)).update({"is_remove": 1},synchronize_session='fetch')

    db.session.commit()
    db.session.close()
    db.session.remove()

    return Result.success_response(msg='删除成功')