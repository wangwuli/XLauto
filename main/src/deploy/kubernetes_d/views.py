import os

from src.dao import hosts
from src.dao.hosts_operation import host_action_execute
from src.deploy import deploy
from multiprocessing import Pool
from src.general.Connect_G import Sshmet
from src.general.General import ReturnG, Result
from flask import request, current_app
from src.general.Sqla import Sqla
from src.general.process_correlation import ProcessPool


@deploy.route('/deploy/kubernetes_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def kubernetes_install():

    configuration_info = request.get_json()

    configuration_info['firewalld'] = 0 if configuration_info['firewalld'] == False else 1
    configuration_info['selinux'] = 0 if configuration_info['selinux'] == False else 1
    configuration_info['powerboot'] = 0 if configuration_info['powerboot'] == False else 1


    sqla = Sqla(current_app)

    sql = """
    SELECT * FROM system_function a
    WHERE a.system_name = :system_name
    AND a.system_version = :system_version
    AND (
    (a.system_action = "firewalld_control" AND a.action_service_switch = :firewalld)
    OR (a.system_action = "selinux_control" AND a.action_service_switch = :selinux)
    OR (a.system_function_id = :repository)
    OR (a.system_function_id = 8)
    OR (a.system_action = "docker_repository")
    OR (a.system_action = "yum_install_docker")
    OR (a.system_action = "enable_docker" AND a.action_service_switch = :powerboot)
    OR (a.system_action = "enable_kubelet" AND a.action_service_switch = :powerboot)
    OR (a.system_action = "start_docker" AND a.action_service_switch = :powerboot)
    OR (a.system_action = "start_kubelet" AND a.action_service_switch = :powerboot)
    )
   order by a.order_by desc
    """
    host_execute_info = sqla.fetch_to_dict(sql, {
        'system_name': configuration_info['system_name'],
        'system_version' : configuration_info['system_version'],
        'firewalld': configuration_info['firewalld'],
        'selinux': configuration_info['selinux'],
        'repository': configuration_info['repository'],
        'powerboot': configuration_info['powerboot']
        })

    system_function_ids = []
    for host_execute_info_one in host_execute_info:
        system_function_ids.append(host_execute_info_one['system_function_id'])

    host_user_infos = []
    for host_id  in configuration_info['host_ids']:
        host_user_info = hosts.get_hotst_connect_info(host_id)
        host_user_infos.append(host_user_info)

    host_action_execute(host_user_infos,system_function_ids)

    return Result.success_response(msg='提交安装申请成功，正在处理')