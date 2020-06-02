# -*- coding: utf-8 -*-
'''
@author: liww
@file: auxiliary.py
@time: 2020/6/1 11:56
@desc:
'''
import os
import time

from models.models import ScriptFileExecuteEvent, db
from src.general.Connect_G import SCPMet

# 连接单台服务器，单台服务器脚本统一处理
def run_script_worker(info_dict, script_list, time_out):
    info_dict['timeout'] = time_out

    ssh = SCPMet()
    ssh.set_info(info_dict)
    ssh_obj = ssh.connect()

    for script_list_one in script_list:
        file_name = os.path.basename(script_list_one['script_file_path'])
        ssh_obj.put_file_exec(script_list_one['script_file_path'], os.path.join('/tmp', file_name), '', type='sh', nohup=False)

        #结果间歇性写入数据库
        for i in range(time_out / 10):
            time.sleep(10)
            file_sql_obj = ScriptFileExecuteEvent(
                script_execute_event_batch_id=info_dict['script_execute_event_batch_id'],
                script_file_id=script_list_one['script_file_id'], script_file_content=ssh.execcmd_out,
                execute_result=ssh.execute_result)
            db.session.add(file_sql_obj)
            db.session.commit()
            db.session.close()

    ssh_obj.close()

    return True
