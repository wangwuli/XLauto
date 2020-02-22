# -*- coding: utf-8 -*-
'''
@author: liww
@file: soft.py
@time: 2019/12/5 10:06
@desc:
'''
import os

from . import deploy
import sys
from multiprocessing import Pool
from ..general.Connect_G import Sshmet
from ..general.General import ReturnG, Result
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
            return ReturnG.return_false(e.strerror)
        info = ssh.execcmd(cmd)
        ssh_c.close()
        return info


class Make(conf_file_pro):
    def install(self, name, othe_parameter):
        result = []
        pool = Pool(5)
        # for i in range(len(othe_parameter["hosts"])):
        #     result.append(pool.apply_async(func=self.ssh_d, args=(
        #     othe_parameter['hosts'], othe_parameter['install_conf'], name)).get())
        # pool.close()
        # pool.join()
        test = self.ssh_d(othe_parameter['hosts'][0], othe_parameter['install_conf'], name)
        return Result.success_response(test)

    def ssh_d(self, hosts_dict, install_conf_dict, soft_name):
        ssh = Sshmet()
        ssh.set_info(hosts_dict)
        try:
            ssh_c = ssh.connect()
        except TimeoutError as e:
            return ReturnG.return_false(e.strerror)
        unzip_info = self.get_unzipdir(ssh, install_conf_dict['file_path'],soft_name)
        if ReturnG.if_ft(unzip_info):
            cmd  = "cd %s && ./configure --with-http_stub_status_module --with-http_ssl_module && make && make install" %unzip_info[1]
            info = ssh.execcmd(cmd)
        else:
            return ReturnG.return_false(unzip_info[1])
        ssh_c.close()
        return info

    def get_unzipdir(self, ssh, file_path, name):
        file_path_tuple = os.path.split(file_path)

        file_type = ssh.execcmd("file --mime-type %s" % file_path)[1]

        if file_type.find("No such file or directory") != -1:
            return ReturnG.return_false('安装文件不存在')
        elif file_type.find("gzip") != -1:
            new_file_path = "%s/%s.tar" %(file_path_tuple[0],name)
            cmd = "gunzip %s -c >  %s" % (file_path, new_file_path)
            file_path = new_file_path
        elif file_type.find("tar") != -1:
            new_file_path = "%s/%s" % (file_path_tuple[0], name)
            cmd = "mkdir {new_file_path} ; tar -xvf {file_path} -C {new_file_path} --strip-components 1".format(file_path=file_path, new_file_path=new_file_path)
            file_path = new_file_path
        elif file_type.find("directory") != -1:
            return ReturnG.return_true(file_path)
        else:
            return ReturnG.return_false("解压失败")

        exe_info = ssh.execcmd(cmd)

        if not ReturnG.if_ft(exe_info):
            exe_info_text = ReturnG.get_value(exe_info)
            if exe_info_text.find("command not found") != -1:
                return ReturnG.return_false(exe_info)

        return self.get_unzipdir(ssh, file_path, name)