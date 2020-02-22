# -*- coding: utf-8 -*-
'''
@author: liww
@file: soft.py
@time: 2019/12/5 10:06
@desc:
'''
from . import deploy
import sys
from multiprocessing import Pool
from ..general.Connect_G import Sshmet
from ..general.General import RETURNG, Result
from flask import request


@deploy.route('/deploy/soft_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def soft_install():
    """
    example json:
    {
    "name": "nginx",
    "type": "yum",
    "othe_parameter":{
        "config":{
            "configaddr": "",
            "configparameter":{"key":"value"},
            "conftype":""
        },
        "hosts":
            [{"ip":"192.168.0.107" ,"username":"root" ,"password":"123456", "port":"22" ,"timeout":"30"}]
    }
    }
    """
    data_dict = request.get_json()
    soft_ = SoftIstall()
    info = soft_.soft_install(data_dict['name'], data_dict['type'], data_dict["othe_parameter"])
    return info


class SoftIstall:
    def soft_install(self, name, type, othe_parameter):
        """
        :param name: The software name
        :param type: Deployment type
        :param othe_parameter: other parameters dict
        :return:
        """
        if type == 'docker':
            return docker(name)
        elif type == 'make':
            make = Make()
            make_info = make.install(name, othe_parameter)
            # yum.template()
            return make_info
        elif type == 'yum':
            yum_ = Yum()
            yum_info = yum_.install(name, othe_parameter)
            # yum.template()
            return yum_info


class conf_file_pro:
    def xml_conf(self):
        return self.name

    def cfg_conf(self):
        return self.name

    def template(self):
        return


class docker(conf_file_pro):
    def __init__(self, name):
        print("docker")


class Yum(conf_file_pro):
    def install(self, name, othe_parameter):
        result = []
        install_cmd = "yum install -y %s" % name
        pool = Pool(5)
        for i in range(len(othe_parameter["hosts"])):
            result.append(pool.apply_async(func=self.ssh_d, args=(othe_parameter['hosts'][i], install_cmd)).get())
        pool.close()
        pool.join()
        # test = self.ssh_d(othe_parameter['hosts'][0],install_cmd)
        return Result.success_response(result)

    def ssh_d(self, host_listinfo, cmd):
        ssh = Sshmet()
        ssh.set_info(host_listinfo)
        try:
            ssh_c = ssh.connect()
        except TimeoutError as e:
            return RETURNG.return_false(e.strerror)
        info = ssh.execcmd(cmd)
        ssh_c.close()
        return info


class Make(conf_file_pro):
    def install(self, name, othe_parameter):
        result = []
        pool = Pool(5)
        for i in range(len(othe_parameter["hosts"])):
            result.append(pool.apply_async(func=self.ssh_d, args=(
            othe_parameter['hosts'], othe_parameter['install_conf'], othe_parameter['name'])).get())
        pool.close()
        pool.join()
        # test = self.ssh_d(othe_parameter['hosts'][0],install_cmd)
        return Result.success_response(result)

    def ssh_d(self, install_conf_dict, cmd):
        ssh = Sshmet()
        ssh.set_info(host_listinfo)
        try:
            ssh_c = ssh.connect()
        except TimeoutError as e:
            return RETURNG.return_false(e.strerror)
        info = ssh.execcmd(cmd)
        ssh_c.close()
        return info
