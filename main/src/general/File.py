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


def str_save_file(file_content_str, file_path=None):
    if not file_path:
        file_path = os.path.join(settings.TMP_PATH, "temporary_file","%s" %str(uuid.uuid1()))
    hooks = open(file_path, 'a')
    hooks.write(file_content_str)
    hooks.close()
    return file_path