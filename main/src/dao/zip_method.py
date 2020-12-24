# -*- coding: utf-8 -*-
'''
@author: liww
@file: zip_method.py
@time: 2020/12/24 15:50
@desc:
'''
from src.general.Zip import zip_c
from src.general.General import ReturnG

def unzip_distinguish(type, file_path, target_path):
    zip_obj = zip_c(file_path, target_path)

    if type == "zip":
        return zip_obj.unzip()
    elif type == "gz":
        return zip_obj.ungzip()
    elif type in ("tgz","tar"):
        return zip_obj.untar()
    else:
        return ReturnG.return_false('不支持的解压类型')

