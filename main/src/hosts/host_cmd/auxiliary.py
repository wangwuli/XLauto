# -*- coding: utf-8 -*-
'''
@author: liww
@file: auxiliary.py
@time: 2020/6/1 11:56
@desc:
'''
import os
import threading
import time

import paramiko
from flask import current_app

from models.models import ScriptFileExecuteEvent, db
from src.general.Sqla import Sqla
from src.general.Connect_G import SCPMet
from src.general.Transform import model_to_dict


def put_file_exec_(ssh, script_file_path, tmp_file_name):
    ssh.put_file_exec(script_file_path, tmp_file_name, '', type='sh', nohup=False)


# 连接单台服务器，单台服务器脚本统一处理
def run_script_worker(info_dict, script_list, time_out):
    try:
        info_dict['timeout'] = time_out

        ssh = SCPMet()
        ssh.set_info(info_dict)
        ssh_obj = ssh.cp_connect()

        for script_list_one in script_list:
            file_name = os.path.basename(script_list_one['script_file_path'])
            p = threading.Thread(target=put_file_exec_, args=(ssh, script_list_one['script_file_path'], os.path.join('/tmp', file_name)))
            p.start()

            # ssh_obj.put_file_exec(script_list_one['script_file_path'], os.path.join('/tmp', file_name), '', type='sh', nohup=False)

            #结果间歇性写入数据库
            for i in range(int(time_out / 10)):
                time.sleep(10)
                # file_sql_obj = ScriptFileExecuteEvent(
                #     script_execute_event_batch_id=info_dict['script_execute_event_batch_id'],
                #     script_file_id=script_list_one['script_file_id'], script_file_content=ssh.execcmd_out,
                #     execute_result=ssh.execute_result,host_id=info_dict['host_id'])
                # db.session.add(file_sql_obj)
                # db.session.commit()
                # db.session.close()

                #新增或者更新数据
                dicts = {
                    'script_execute_event_batch_id': info_dict['script_execute_event_batch_id'],
                    'script_file_id': script_list_one['script_file_id'],
                    'script_file_content': ssh.execcmd_out,
                    'execute_result': ssh.execute_result,
                    'host_id': info_dict['host_id']
                }
                data = db.session.query(ScriptFileExecuteEvent).filter_by(script_execute_event_batch_id=info_dict['script_execute_event_batch_id'],
                                                                          script_file_id=script_list_one['script_file_id'],
                                                                          host_id=info_dict['host_id']
                                                                          ).first()
                if data:
                    {setattr(data, k, v) for k, v in dicts.items()}
                    print(data)
                else:
                    db.session.execute(ScriptFileExecuteEvent.__table__.insert(), dicts)
                db.session.commit()

                if ssh.execute_result: break

        ssh_obj.close()
        return True

    except paramiko.ssh_exception.SSHException as e:
        for script_list_one in script_list:
            file_sql_obj = ScriptFileExecuteEvent.query.filter_by(
                script_execute_event_batch_id=info_dict['script_execute_event_batch_id'],
                script_file_id=script_list_one['script_file_id']).first()
            file_sql_obj.script_file_content = e
            file_sql_obj.execute_result = -1
            db.session.add(file_sql_obj)
        db.session.commit()
        db.session.close()
        return False

def query_execute_batch_status(script_execute_event_batch_id):
    """
    查询批次状态
    :param script_execute_event_batch_id:
    :return:
    """
    sys_code_data = db.session.query(ScriptFileExecuteEvent.script_file_id, ScriptFileExecuteEvent.execute_result,
                                     ScriptFileExecuteEvent.script_file_content, ScriptFileExecuteEvent.host_id).filter(
        ScriptFileExecuteEvent.script_execute_event_batch_id == script_execute_event_batch_id).all()
    db.session.close()
    data = model_to_dict(sys_code_data)

    return data
