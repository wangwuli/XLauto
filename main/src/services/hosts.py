# -*- coding: utf-8 -*-
from flask import request

from src.general.General import Result
from src.services import services
from src.services.auxiliary import host_info_query


@services.route('/hosts/info_query', methods=['GET'])
def hostinfo_query():
    parameter_dict = request.args.to_dict()
    #parameter_dict = request.json

    data = host_info_query(parameter_dict['host_id'])

    return Result.success_response(data, '查询主机信息成功')