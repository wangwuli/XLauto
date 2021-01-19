# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: file.py
@time: 2020/6/1 10:46
@desc:
'''
import os
import uuid
import settings


#将字符串保存为文件
def str_save_file(file_content_str, file_path=None):
    if not file_path:
        file_path = os.path.join(settings.TMP_PATH, "temporary_file","%s" %str(uuid.uuid1()))
    hooks = open(file_path, 'a')
    hooks.write(file_content_str)
    hooks.close()
    return file_path


def str_sin_file(file_path, str):
    hooks = open(file_path, 'a')
    hooks.write(str)
    hooks.close()


def get_dir_file(dirname):
    """
    返回目录下所有文件
    :param dirname:
    :return:
    """
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        maindir = maindir.replace('\\', '/')
        result.append(maindir + '/')
        for filename in file_name_list:
            apath = os.path.join(maindir, filename).replace('\\', '/')
            result.append(apath)

    return result