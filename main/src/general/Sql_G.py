# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: Sql_G.py
@time: 2019/12/3 17:14
@desc:
'''
import pymysql
from flask import app

import settings


def mysql_sql_exec(cmd, args = []):
    conn = pymysql.Connection(host=settings.database_service_ip, database=settings.database_name,
                              user=settings.database_user, password=settings.database_pwd,
                              port=int(settings.database_service_port), charset='utf8')
    cursor = conn.cursor()

    if len(args) == 0:
        cursor.execute(cmd)
    else:
        cursor.execute(cmd, args)

    conn.commit()
    cursor.close()
    row_list = []

    if cursor._rows != None:
        for nu_one in range(len(cursor._rows)):
            row_list.append({})

        for rows_one in cursor._rows:
            i_a = 0
            i = 0
            for description_one in cursor.description:
                dict_swap = {description_one[0]: rows_one[i]}
                try:
                    row_list[i_a] = dict(row_list[i_a], **dict_swap)
                except:
                    pass
                i += 1
            i_a += 1

    return row_list
