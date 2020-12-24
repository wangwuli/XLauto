# -*- coding: utf-8 -*-
'''
@author: liww
@file: Zip.py
@time: 2020/12/24 11:01
@desc:
'''

import gzip
import os
import tarfile
import zipfile

from src.general.General import ReturnG


class zip_c():
    def __init__(self, file_path, target_path):
        """
        初始化值
        :param file_path: 文件完整路径
        :param target_path: 目标路径，解压路径或者压缩文件路径
        """
        self.file_name =  file_path.split('.')[0]
        self.file_path = file_path
        self.target_path = target_path
        self.target_path_name = os.path.join(target_path, self.file_name)
        if not os.path.exists(self.target_path_name):
            os.makedirs(self.target_path_name)

    def ungzip(self):
        file_obj = gzip.GzipFile(self.file_path)
        open(self.target_path_name, "w+").write(file_obj.read())
        file_obj.close()
        return self.target_path_name

    def untar(self):
        file_obj = tarfile.open(self.file_path, 'r')
        file_obj.extractall(self.target_path_name)
        file_obj.close()
        return self.target_path_name


    def unzip(self):
        r = zipfile.is_zipfile(self.file_path)
        if r:
            fz = zipfile.ZipFile(self.file_path, 'r')
            for file in fz.namelist():
                fz.extract(file, self.target_path)
        else:
            return ReturnG.return_false('这不是一个zip包，请先核实')
        return self.target_path_name

