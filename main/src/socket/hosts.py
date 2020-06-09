# -*- coding: utf-8 -*-
import json

from flask import request

from src.general.General import Result
from src.hosts.host_cmd.auxiliary import query_execute_batch_status
from src.socket import socket
from src.services.auxiliary import host_info_query


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



@socket.route('/socket/hosts/execute_script_query')
def execute_script_query(ws):
    while not ws.closed:
        message = ws.receive()
        try:
            parameter_dict = eval(message)
            data = {'data': query_execute_batch_status(parameter_dict['script_execute_event_batch_id']), "success":1, "msg": "加载主机信息成功"}
            # {"msg": "%s" %e, "success":0, "data": host_info_query(parameter_dict['host_id'])}
        except Exception as e:
            data = {"msg": "%s" %e, "success":0,}

        ws.send(json.dumps(data))