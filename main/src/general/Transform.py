#sqlalchemy 查询结果转为字典
from datetime import datetime

from sqlalchemy.orm import class_mapper


# def model_to_dict(result):
#     from collections import Iterable
#     # 转换完成后，删除  '_sa_instance_state' 特殊属性
#     try:
#         if isinstance(result, Iterable):
#             tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
#             for t in tmp:
#                 t.pop('_sa_instance_state')
#         else:
#             tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
#             tmp.pop('_sa_instance_state')
#         return tmp
#     except BaseException as e:
#         print(e.args)
#         raise TypeError('Type error of parameter')


def model_to_dict(obj):
    return_list = []
    if len(obj) != 0:
        fields = obj[0]._fields
        for obj_one in obj:
            data_one = dict(zip(fields,obj_one))
            return_list.append(data_one)
    return return_list
