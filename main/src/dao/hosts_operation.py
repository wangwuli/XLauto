# -*- coding: utf-8 -*-
'''
@author: liww
@file: hosts_operation.py
@time: 2020/7/31 11:32
@desc:
'''
from src.general.Connect_G import Sshmet
from flask import current_app
from main.models.models import SystemFunction, db
from src.general.Transform import model_to_dict
from src.general.process_correlation import ProcessPool
from jinja2 import Template


def host_action_execute(host_user_infos, system_function_ids, replace_parameters=''):
    """
    执行具体命令表ID动作
    :param host_id:
    :param system_function_id: system_function.system_function_id
    :return:
    """

    pool = ProcessPool()

    system_function_info = db.session.query(SystemFunction.system_function_id,
                                            SystemFunction.function_type,
                                            SystemFunction.system_content,
                                            SystemFunction.system_content_file,
                                            SystemFunction.action_service_switch,
                                            ).filter(
        SystemFunction.system_function_id.in_(system_function_ids)).all()

    system_function_info = model_to_dict(system_function_info)

    start_list = []
    for host_user_info in host_user_infos:
        start_list_one = {'host_user_info': host_user_info, 'system_function_info': system_function_info,
                          'replace_parameters': replace_parameters}
        start_list.append(start_list_one)
    pool.start(exec_start, start_list)
    return True


def exec_start(host_user_info, system_function_info, replace_parameters):

    ssh_m = Sshmet()
    ssh_m.set_info(host_user_info)
    ssh_m.connect()

    for system_function_one in system_function_info:
        if system_function_one['function_type'] == 'cmd':
            info = ssh_m.execcmd(system_function_one['system_content'])
            current_app.logger.info("[system_function]执行：%s 结果：%s" % (system_function_one['system_content'], info))

        elif system_function_one['function_type'] == 'addfile':
            info = ssh_m.execcmd(
                "echo %s > %s" % (system_function_one['system_content'], system_function_one['system_content_file']))
            current_app.logger.info("[system_function]执行： echo %s > %s  结果：%s" % (
                system_function_one['system_content'], system_function_one['system_content_file'], info))

        elif system_function_one['function_type'] == 'cmdp':
            system_content = Template(system_function_one['system_content']).render(replace_parameters)
            info = ssh_m.execcmd(system_content)
            current_app.logger.info("[system_function]执行：%s 结果：%s" % (system_function_one['system_content'], info))

    ssh_m.close()