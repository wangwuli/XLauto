# -*- coding: utf-8 -*-
import json

from flask import request

from src.general.General import Result
from src.socket import socket
from src.services.auxiliary import host_info_query


# @services.route('/hosts/info_query', methods=['GET'])
@socket.route('/socket/hosts/info_query')
def hostinfo_query(ws):
    while not ws.closed:
        message = ws.receive()
        try:
            parameter_dict = eval(message)
            data = {'data': host_info_query(parameter_dict['host_id']), "success":1, "msg": "加载主机信息成功"}
            # {"msg": "%s" %e, "success":0, "data": host_info_query(parameter_dict['host_id'])}
        except Exception as e:
            data = {"msg": "%s" %e, "success":0,}

        ws.send(json.dumps(data))

    #parameter_dict = request.args.to_dict()
    #parameter_dict = request.json

    #data = host_info_query(parameter_dict['host_id'])

    #return Result.success_response(data, '查询主机信息成功')