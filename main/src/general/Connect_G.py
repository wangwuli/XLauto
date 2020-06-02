# -*- coding: utf-8 -*-
'''
@author: liww
@file: Connect_G.py
@time: 2019/12/5 17:02
@desc:
'''
from itertools import zip_longest
import os
import shlex
import subprocess
import uuid

import paramiko


class Sshmet():
    #测试调整，待完善
    def __init__(self):
        self.execcmd_out = ''   #执行结果
        self.execute_result = 0   # 0失败 1成功 2警告

        self.ip = None
        self.username = None
        self.password = None
        self.port = None
        self.timeout = 30

    def set_info(self, host_info_dict):
        self.ip = host_info_dict["host_ip"]
        self.username = host_info_dict["user_name"]
        self.password = host_info_dict["user_pass"]
        self.port = host_info_dict["host_port"]
        self.timeout = host_info_dict.get("timeout") and host_info_dict["timeout"] or self.timeout

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.username, self.password, timeout=int(self.timeout), banner_timeout=10)
        return self.ssh

    def execcmd(self, cmd):
        """/
        执行单条命令,等待完成输出
        :param cmd:
        :return:
        """
        # env = 'source .bash_profile;source /etc/profile;export LANG=en_US.UTF-8;'
        # stdin, stdout, stderr = self.ssh.exec_command('%s%s' % (env, cmd))
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        stdout = str(stdout.read(),'utf-8')
        stderr = str(stderr.read(),'utf-8')
        #result = ''.join(stdout.read() + stderr.read())
        result = (stdout+ stderr).strip()
        if not stderr == '':
            result = False
        return result

    def runcrealtime(self, command, callback=None):
        """
        实时执行命令
        :param command:  命令
        :param callback: 回调函数
        :return:
        """
        #回调函数默认收集为class.execcmd_out变量
        if not callback:
            callback = self.execcmdout

        stdin, stdout, stderr = self.ssh.exec_command(
            command, bufsize=1
        )

        stdout_iter = iter(stdout.readline, '')
        stderr_iter = iter(stderr.readline, '')

        err_status = 0
        out_status = 0
        #标准输出
        for line in stdout_iter:
            callback(line.strip())
            out_status = 1
        #标准输出结束后收集错误输出
        for line in stderr_iter:
            callback(line.strip())
            err_status = 1

        if out_status == 1 and err_status == 1:
            self.execute_result = 2
        elif err_status == 1:
            self.execute_result = 0
        else:
            self.execute_result = 1

        # test = zip_longest(stdout_iter, stderr_iter)
        # for out, err in zip(stdout_iter, stderr_iter):
        #     if out: callback(out.strip())
        #     if err: callback(err.strip())

        return stdin, stdout, stderr

    def execcmdout(self, text):
        self.execcmd_out += str(text)
        print(str(text))


    def close(self):
        self.ssh.close()


class SCPMet(Sshmet):

    def connect(self):
        self.ssh = paramiko.Transport((self.ip, self.port))
        self.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.ssh)
        return self.sftp

    def get_file(self, src_file, des_file):
        self.sftp.get(src_file, des_file)
        return des_file

    def progress_bar(self, transferred, toBeTransferred, suffix=''):
        bar_len = 100
        filled_len = int(round(bar_len * transferred / float(toBeTransferred)))
        percents = round(100.0 * transferred / float(toBeTransferred), 1)
        self.percents = percents

    def put_file(self, src_file, des_file):
        self.sftp.put(src_file, des_file, callback=self.progress_bar)

        # all_files = self.__get_all_files_in_local_dir(local_dir)
        # for x in all_files:
        #     filename = os.path.split(x)[-1]
        #     remote_filename = remote_dir + '/' + filename
        #     print
        #     u'Put文件%s传输中...' % filename
        #     sftp.put(x, remote_filename)

        return des_file

    def put_file_exec(self, src_file, des_file, param, type='sh',nohup=True, callback=None):
        """
        上传文件并执行
        :param src_file: 源文件
        :param des_file: 目标文件
        :param param: 脚本参数
        :param type:  python or sh ?
        :return:
        """
        self.put_file(src_file, des_file)

        file_name = str(uuid.uuid1())

        if nohup:
            cmd = 'nohup %s %s %s > %s 2>&1 &' % (type, des_file, param, file_name)
            cmd_result = self.execcmd(cmd)
        else:
            cmd = '%s %s %s' % (type, des_file, param)
            cmd_result = self.runcrealtime(cmd, callback)

        return cmd_result

    def list_dir(self, dir_name):
        return self.sftp.listdir(dir_name)

    def __get_all_files_in_local_dir(self, local_dir):
        all_files = list()
        files = os.listdir(local_dir)
        for x in files:
            filename = os.path.join(local_dir, x)
            if os.path.isdir(x):
                all_files.extend(self.__get_all_files_in_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files



class Ip_c():
    def __init__(self):
        self.succeed = True

    def string_formatting(self, ipstr):
        """
        解析连续IP字符，返回数组
        :param ipstr: 192.168.0.1-192,192.168.0.199
        :return:
        """
        ip_addrs = []
        for ipstr_one in ipstr.split(','):
            if ipstr_one.find('-') != -1:
                basket_dict_one_separation = ipstr_one.split('-')
                if self.if_ipaddr(basket_dict_one_separation[0]) and len(str(basket_dict_one_separation[1]) < 4):
                    start_number = basket_dict_one_separation[0].split(".")[-1]
                    start_number_s = basket_dict_one_separation[0].rstrip(start_number)
                    for number_one in range(int(start_number) , int(basket_dict_one_separation[1]) + 1):
                        ip_addrs.append(start_number_s + str(number_one))
            else:
                if self.if_ipaddr(ipstr_one):
                    ip_addrs.append(ipstr_one)
        return ip_addrs

    def if_ipaddr(self, ip):
        """
        判断字符串是否为IP
        :param ipstr: 192.168.0.1
        :return:
        """
        ip_split = ip.split('.')
        if not len(ip_split) == 4:
            self.succeed = False
        for ip_split_one in ip_split:
            if not 0 < int(ip_split_one) < 255:
                self.succeed = False
        return ip