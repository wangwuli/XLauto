# -*- coding: utf-8 -*-
'''
@author: liww
@file: update_file.py
@time: 2020/5/15 14:41
@desc:
'''
import os
import threading
import uuid

from flask import request, current_app
from models.models import ScriptFileCabinet, db, SysCode
from src.dao.hosts import get_hotst_connect_info
from src.general.Connect_G import Sshmet, SCPMet
from src.general.File import str_save_file
from src.general.General import Result
from src.general.Sqla import Sqla
from src.general.Transform import model_to_dict
from src.hosts import hosts
from src.hosts.host_cmd.auxiliary import run_script_worker


@hosts.route('/hosts/update_script_file', methods=['POST'])
def update_script_file():
    f_obj = request.files['file']
    current_app_ = current_app
    script_path = os.path.join(current_app_.config.xlautoenv['PROJECT_PATH'], current_app_.config['DATA_PATH'], 'scriptfiles')
    if not os.path.exists(script_path):
        os.makedirs(script_path)

    script_path_file = os.path.join(script_path, str(uuid.uuid1()))

    file_sql_obj = ScriptFileCabinet(script_file_path=script_path_file, script_file_name=f_obj.filename)
    db.session.add(file_sql_obj)
    db.session.commit()
    db.session.close()

    f_obj.save(script_path_file)

    return Result.success_response(msg='上传成功')


@hosts.route('/hosts/update_script_query', methods=['GET'])
def update_script_query():
    script_file_group = request.args.get('script_file_group')
    script_file_type = request.args.get('script_file_type')

    if script_file_group:
         sql_file_group, sql_file_group_null = '%%%s%%' % script_file_group, ''
    else:
        sql_file_group, sql_file_group_null = '%', 'OR a.script_file_type IS NULL'

    if script_file_type:
        sql_file_type, sql_file_type_null = '%%%s%%' % script_file_type, ''
    else:
        sql_file_type, sql_file_type_null = '%', 'OR a.script_file_group IS NULL'


    sql_parameter = {"script_file_group" :sql_file_group, "script_file_type": sql_file_type}
    sql = """
    SELECT * FROM script_file_cabinet a
    WHERE (a.script_file_type LIKE :script_file_type %s)
    AND (a.script_file_group LIKE :script_file_group %s)
    """ %(sql_file_type_null, sql_file_group_null)
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, sql_parameter)

    # update_script_obj = db.session.query(ScriptFileCabinet.id, ScriptFileCabinet.script_file_path, DocumentCabinet.script_file_name,
    #                                ScriptFileCabinet.script_file_group, ScriptFileCabinet.script_file_type, DocumentCabinet.comment, ).all()
    # db.session.close()
    # project_data = model_to_dict(update_script_obj)

    return Result.success_response(data=data, msg='查询成功')


@hosts.route('/hosts/rm_script', methods=['DELETE'])
def rm_script():
    id = request.json.get('id')
    delete_script_obj = ScriptFileCabinet.query.filter(ScriptFileCabinet.id==id).first()

    os.remove(delete_script_obj.script_file_path)

    db.session.delete(delete_script_obj)
    db.session.commit()
    db.session.close()

    return Result.success_response(msg='删除成功')


@hosts.route('/hosts/edit_script', methods=['POST'])
def edit_script():
    data_dict = request.get_json()

    delete_script_obj = ScriptFileCabinet.query.filter_by(id=data_dict['id']).first()
    delete_script_obj.script_file_group = data_dict['script_file_group']
    delete_script_obj.script_file_type = data_dict['script_file_type']

    db.session.commit()
    db.session.close()

    return Result.success_response(msg='修改成功')



@hosts.route('/hosts/script_execute_query_history', methods=['GET'])
def script_execute_query_history():
    script_file_name = request.args.get('script_file_name')

    if script_file_name:
        sql_fragment = "WHERE b.script_file_name LIKE  :script_file_name"
    else:
        sql_fragment = ''

    sql = """
    SELECT 
    a.script_file_execute_event_id,
    a.script_execute_event_batch_id,
    a.execute_time,
    a.execute_end_time,
    a.script_file_id,
    a.script_file_content,
    b.script_file_name,
    c.code_name AS script_file_execute_result_text
    FROM script_file_execute_event a
    LEFT JOIN  script_file_cabinet b ON a.script_file_id = b.script_file_id
    LEFT JOIN sys_code c ON c.code_key = a.execute_result AND c.code_type = "script_file_execute_result_ype"
    %s
    """ %sql_fragment
    sqla = Sqla(current_app)

    data = sqla.fetch_to_dict(sql, {'script_file_name': '%%%s%%' %script_file_name})

    return Result.success_response(data=data, msg='查询成功')



@hosts.route('/hosts/execute_script', methods=['POST'])
def execute_script():
    data_dict = request.get_json()

    hosts_table_data = data_dict['hosts_table_data']
    timeout = data_dict['hosts_table_data']

    if not timeout:
        timeout = 3600

    #生成执行批次ID
    script_execute_event_batch_id = str(uuid.uuid1())

    for hosts_table_data_one in hosts_table_data:

        existing_script_total_list = hosts_table_data_one.get('existing_script_total')
        history_script_total_list = hosts_table_data_one.get('history_script_total')
        temporary_script_total_str = hosts_table_data_one.get('temporary_script_total')

        #获取主机信息
        host_id = hosts_table_data_one['host_id']
        info_dict = get_hotst_connect_info(host_id)
        info_dict['script_execute_event_batch_id'] = script_execute_event_batch_id

        #拼接此主机下各类脚本信息
        script_total_list = []
        if existing_script_total_list:
            script_total_list += existing_script_total_list
        if history_script_total_list:
            script_total_list += history_script_total_list
        if temporary_script_total_str:
            for temporary_script_total_str_one in temporary_script_total_str:
                temporary_script_total_str_one['script_file_path'] = str_save_file(temporary_script_total_str_one['script_file_content'])

            script_total_list += temporary_script_total_str

        run_script_worker(info_dict, script_total_list, timeout)
        # p = threading.Thread(target=run_script_worker, args=(info_dict, script_total_list, timeout))
        # p.start()



    return Result.success_response(msg='请求成功')