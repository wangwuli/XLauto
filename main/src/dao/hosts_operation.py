# -*- coding: utf-8 -*-
'''
@author: liww
@file: hosts_operation.py
@time: 2020/7/31 11:32
@desc:
'''
from src.dao import hosts
from src.general.Connect_G import Sshmet
from src.general.Sqla import Sqla
from flask import current_app
from main.models.models import SystemFunction, db


async def host_action_execute(host_id, system_function_ids):
    """
    执行具体命令表ID动作
    :param host_id:
    :param system_function_id: system_function.system_function_id
    :return:
    """

    host_user_info = hosts.get_hotst_connect_info(host_id)

    system_function_info = db.session.query(SystemFunction.system_function_id,
                                            SystemFunction.function_type,
                                            SystemFunction.system_content,
                                            SystemFunction.system_content_file,
                                            SystemFunction.action_service_switch,
                                            ).filter(
        SystemFunction.system_function_id.in_(system_function_ids)).all()

    for system_function_one in system_function_info:
        if system_function_one['function_type'] == 'cmd':
            ssh_m = Sshmet()
            ssh_m.set_info(host_user_info)
            ssh_m.connect()
            info = ssh_m.execcmd(system_function_one['system_content'])
            ssh_m.close()

            current_app.logger.info("[system_function]执行：%s 结果：%s" % (system_function_one['system_content'], info))

        elif system_function_one['function_type'] == 'addfile':
            ssh_m = Sshmet()
            ssh_m.set_info(host_user_info)
            ssh_m.connect()
            info = ssh_m.execcmd(
                "echo %s > %s" % (system_function_one['system_content'], system_function_one['system_content_file']))
            ssh_m.close()

            current_app.logger.info("[system_function]执行： echo %s > %s  结果：%s" % (
            system_function_one['system_content'], system_function_one['system_content_file'], info))


    return True