# -*- coding: utf-8 -*-
from flask import request

from main.models.models import HostInstance, SysCode, db, SysMenu, Project
from src.services.auxiliary import home_hosts_query_filter
from . import services
from src.general.General import Result
from src.general.Transform import model_to_dict, list_to_tree


@services.route('/home/menu_query', methods=['GET'])
def home_menu_query():

    sys_menu = db.session.query(SysMenu.id,SysMenu.parent_id,SysMenu.name,SysMenu.icon,SysMenu.title).all()
    db.session.close()
    sys_menu_data = model_to_dict(sys_menu)

    data = list_to_tree(sys_menu_data)

    return Result.success_response(data,'菜单加载成功')


#主机列表查询
@services.route('/home/hosts_query', methods=['GET'])
def home_hosts_query():
    parameter_dict = request.args.to_dict()

    data = home_hosts_query_filter(parameter_dict)
    # host_obj = db.session.query(HostInstance.host_id, HostInstance.host_ip,
    #                             HostInstance.host_name,SysCode.code_name.label('type_name')).join(
    #                             HostInstance,HostInstance.host_type == SysCode.code_key).filter(
    #                             SysCode.code_type == "host_type")\
    #                             .all()
    # data = model_to_dict(host_obj)

    db.session.close()
    return Result.success_response(data, '目标主机加载成功')



@services.route('/home/projects', methods=['GET'])
def home_projects_query():
    project_obj = db.session.query(Project.project_id, Project.project_name, Project.project_code,
                                    Project.controller_ip, Project.order_id, Project.comments, ).all()
    db.session.close()
    project_data = model_to_dict(project_obj)
    return Result.success_response(project_data,'项目查询成功')