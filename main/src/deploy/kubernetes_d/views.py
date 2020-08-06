import os

from src.deploy import deploy
from multiprocessing import Pool
from src.general.Connect_G import Sshmet
from src.general.General import ReturnG, Result
from flask import request, current_app
from src.general.Sqla import Sqla


@deploy.route('/deploy/kubernetes_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def kubernetes_install():

    configuration_info = request.get_json()

    configuration_info['firewalld'] = 0 if configuration_info['firewalld'] == False else 1
    configuration_info['selinux'] = 0 if configuration_info['selinux'] == False else 1


    sqla = Sqla(current_app)

    sql = """
    SELECT * FROM system_function a
    WHERE a.system_name = :system_name
    AND a.system_version = :system_version
    AND (
    (a.system_action = "firewalld_control" AND a.action_service_switch = :firewalld)
    OR (a.system_action = "selinux_control" AND a.action_service_switch = :selinux)
    )
    """
    host_user_info = sqla.fetch_to_dict(sql, {
        'system_name': configuration_info['system_name'],
        'system_version' : configuration_info['system_version'],
        'firewalld': configuration_info['firewalld'],
        'selinux': configuration_info['selinux'],
        })

    return Result.success_response(msg='安装成功')