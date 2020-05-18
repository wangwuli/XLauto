# -*- coding: utf-8 -*-
'''
@author: liww
@file: update_file.py
@time: 2020/5/15 14:41
@desc:
'''
import os
import uuid

from flask import request, current_app
from models.models import DocumentCabinet, db, SysCode
from src.general.General import Result
from src.general.Sqla import Sqla
from src.general.Transform import model_to_dict
from src.hosts import hosts


@hosts.route('/hosts/update_script_file', methods=['POST'])
def update_script_file():
    f_obj = request.files['file']
    current_app_ = current_app
    script_path = os.path.join(current_app_.config.xlautoenv['PROJECT_PATH'], current_app_.config['DATA_PATH'], 'scriptfiles')
    if not os.path.exists(script_path):
        os.makedirs(script_path)

    script_path_file = os.path.join(script_path, str(uuid.uuid1()))

    file_sql_obj = DocumentCabinet(file_path=script_path_file, file_name=f_obj.filename)
    db.session.add(file_sql_obj)
    db.session.commit()
    db.session.close()

    f_obj.save(script_path_file)

    return Result.success_response(msg='上传成功')


@hosts.route('/hosts/update_script_query', methods=['GET'])
def update_script_query():
    file_group = request.args.get('file_group')
    file_type = request.args.get('file_type')

    sql_file_group = '%%%s%%' %file_group if file_group else  '%'
    sql_file_type = '%%%s%%' % file_type if file_type else '%'


    sql_parameter = {"file_group" :sql_file_group, "file_type": sql_file_type}
    sql = """
    SELECT * FROM document_cabinet a
    WHERE a.file_type LIKE :file_type
    AND a.file_group LIKE :file_group
    """
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, sql_parameter)

    # update_script_obj = db.session.query(DocumentCabinet.id, DocumentCabinet.file_path, DocumentCabinet.file_name,
    #                                DocumentCabinet.file_group, DocumentCabinet.file_type, DocumentCabinet.comment, ).all()
    # db.session.close()
    # project_data = model_to_dict(update_script_obj)

    return Result.success_response(data=data, msg='查询成功')


@hosts.route('/hosts/rm_script', methods=['DELETE'])
def rm_script():
    id = request.json.get('id')
    delete_script_obj = DocumentCabinet.query.filter(DocumentCabinet.id==id).first()

    os.remove(delete_script_obj.file_path)

    db.session.delete(delete_script_obj)
    db.session.commit()
    db.session.close()

    return Result.success_response(msg='删除成功')


@hosts.route('/hosts/edit_script', methods=['POST'])
def edit_script():
    data_dict = request.get_json()

    delete_script_obj = DocumentCabinet.query.filter_by(id=data_dict['id']).first()
    delete_script_obj.file_group = data_dict['file_group']
    delete_script_obj.file_type = data_dict['file_type']

    db.session.commit()
    db.session.close()

    return Result.success_response(msg='修改成功')