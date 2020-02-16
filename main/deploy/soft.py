# -*- coding: utf-8 -*-
'''
@author: liww
@file: soft.py
@time: 2019/12/5 10:06
@desc:
'''
from . import deploy
import sys
from  multiprocessing import Pool
from ..general.Connect_G import Sshmet
from ..general.General import RETURNG
from flask import request


@deploy.route('/deploy/soft_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def soft_install():
    data_dict = request.get_json()
    soft_ = SoftIstall()
    info = soft_.soft_install(data_dict['name'],data_dict['type'],data_dict["othe_parameter"])
    return info


class SoftIstall:
    """
    name: 软件名称,
    type: 部署方式,
    othe_parameter:{
        config:{
            configaddr: { 配置文件相对路径 },
            configparameter:{"key":"value",{{ 配置文件参数 }:{ 设置值 }},
            conftype: {  配置文件格式类型（ini、cfg、xml、config..） } },
        }
        hosts:[{"ip":"" ,"username":"" ,"password":"", "port":"" ,"timeout":""},{}..]
    }
    """

    def soft_install(self, name, type, othe_parameter):
        if type == 'docker':
            return docker(name)
        elif type == 'make':
            return make(name)
        elif type == 'yum':
            if sys.platform.find("linux") == 0:
                return RETURNG.return_false("windows服务器暂时不支持yum安装。")
            yum_ = Yum()
            yum_info = yum_.yum_install(name, othe_parameter)
            #yum.template()
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
    def yum_install(self, name, othe_parameter):
        result=[]
        install_cmd = "yum install -y %s" % name
        # pool = Pool(5)
        # for i in range(len(othe_parameter["hosts"])):
        #     result.append(pool.apply_async(func=self.ssh_d, args=(othe_parameter['hosts'][i],install_cmd)))
        # pool.close()
        # pool.join()
        test = self.ssh_d(othe_parameter['hosts'][0],install_cmd)
        return test


    def ssh_d(self, host_listinfo, cmd):
        ssh = Sshmet()
        ssh.set_info(host_listinfo)
        ssh_c = ssh.connect()
        info = ssh.execcmd(cmd)
        ssh_c.close()
        return info



class make(conf_file_pro):
    def __init__(self, name):
        print("make")
