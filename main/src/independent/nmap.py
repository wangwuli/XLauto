# -*- coding: utf-8 -*-
'''
@author: liww
@file: nmap.py
@time: 2019/12/11 14:55
@desc:
'''
from urllib import request
from . import independent
import telnetlib

from src.general.Connect_G import Ip_c
from src.general.General import Result


@independent.route('/independent/nmap',methods=['GET'])
def nmap():
    data_dict = request.get_json()

    return_dict = {
        "succeed" : {},
        "defeated": {}
    }
    ip_c = Ip_c()
    ip_list = ip_c.string_formatting(data_dict['ips'])

    for host in ip_list:
        for port in data_dict['post'].split(','):
            if get_ip_status(host, port):
                return_dict["succeed"][host] = port
            else:
                return_dict["defeated"][host] = port

    return Result.success_response(return_dict)


def get_ip_status(ip, port):
    server = telnetlib.Telnet()  # 创建一个Telnet对象
    try:
        server.open(ip, port)  # 利用Telnet对象的open方法进行tcp链接
        return_v = True
    except Exception as err:
        return_v = False
    finally:
        server.close()
        return return_v

