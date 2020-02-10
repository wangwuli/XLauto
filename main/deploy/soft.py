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


@deploy.route('/deploy/soft_install', methods=['GET', 'POST', 'PUT', 'DELETE'])
def soft_install():
    return "test"


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

    def get_soft(self, name, type, othe_parameter):
        if type == 'docker':
            return docker(name)
        elif type == 'make':
            return make(name)
        elif type == 'yum':
            if sys.platform.find("linux") == 0:
                return RETURNG.return_false("windows服务器暂时不支持yum安装。")
            yum(name, othe_parameter)
            return True


class conf_file_pro:
    def __init__(self):
        self.name = None
        self.conf_type = None

    def xml_conf(self):
        return self.name

    def cfg_conf(self):
        return self.name

    def template(self):
        return


class docker(conf_file_pro):
    def __init__(self, name):
        print("docker")


class yum(conf_file_pro):
    def __init__(self, name, othe_parameter):
        result=[]
        install_cmd = "yum install -y %s" % name
        pool = Pool(5)
        for i in range(len(othe_parameter["hosts"])):
            result.append(pool.apply_async(func=self.ssh_d, args=(othe_parameter['hosts'][i],install_cmd)))
        pool.close()
        pool.join()
        return result

    def ssh_d(self, host_listinfo, cmd):
        ssh = Sshmet()
        ssh.set_info(host_listinfo)
        info = ssh.execcmd(cmd)
        ssh.close()
        return info



class make(conf_file_pro):
    def __init__(self, name):
        print("make")
