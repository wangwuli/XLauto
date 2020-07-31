# -*- coding: utf-8 -*-

from main.models.models import SysCode, db, SystemFunction
from src.general.General import Result
from src.general.Transform import model_to_dict
from . import services
from flask import request


#码表查询通用接口
@services.route('/general/code_query', methods=['GET'])
def code_query():
    code_type = request.args.get('code_type')

    sys_code_data = db.session.query(SysCode.code_id, SysCode.code_key, SysCode.code_name).filter(
        SysCode.code_type == code_type).all()
    db.session.close()
    data = model_to_dict(sys_code_data)

    return Result.success_response(data,'类型查询成功')


#命令查询通用接口
@services.route('/general/system_action_query', methods=['GET'])
def system_action_query():
    system_action = request.args.get('system_action')

    sys_code_data = db.session.query(SystemFunction.system_function_id, SystemFunction.system_action_name).filter(
        SystemFunction.system_action == system_action).all()
    db.session.close()
    data = model_to_dict(sys_code_data)

    return Result.success_response(data,'类型查询成功')