# -*- coding: utf-8 -*-
'''
@author: liww
@file: auxiliary.py
@time: 2020/6/1 11:56
@desc:
'''
import os

from src.general.Connect_G import SCPMet


def run_script_worker(host_info_dict, script_list, time_out):
    # 连接服务器，统一处理
    ssh = SCPMet()
    ssh.set_info(host_info_dict)
    ssh_obj = ssh.connect()

    for script_list_one in script_list:
        file_name = os.path.basename(script_list_one['script_file_path'])
        ssh_obj.put_file_exec(script_list_one['script_file_path'], os.path.join('/tmp', file_name), '', type='sh', nohup=True)

    return True
