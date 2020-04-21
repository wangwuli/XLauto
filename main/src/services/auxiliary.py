from src.general.LinuxShell import ServerInfo
from src.general.Sql_G import mysql_sql_exec
from src.general.Sqla import Sqla
from flask import current_app


def home_hosts_query_filter(parameter_dict):

    sql_fragment = ''
    sql_parameter = {}
    if parameter_dict['host_project'] != '':
        sql_fragment += "AND a.host_project = :host_project "
        sql_parameter['host_project'] = parameter_dict['host_project']

    if parameter_dict['host_type'] != '':
        sql_fragment += "AND a.host_type_key = :host_type "
        sql_parameter['host_type'] = parameter_dict['host_type']

    if parameter_dict['host_ip'] != '':
        sql_fragment += "AND a.host_ip LIKE :host_ip "
        sql_parameter['host_ip'] = '%%%s%%' %parameter_dict['host_ip']

    sql_fragment += "LIMIT :start,:size "
    size = int(parameter_dict["size"])
    page = int(parameter_dict["page"])
    start = (page - 1) * size
    sql_parameter['start'] = start
    sql_parameter['size'] = size


    sql = """
    SELECT sql_calc_found_rows a.host_id,a.host_ip,a.host_name,b.code_name AS host_type_text,c.project_name FROM host_instance a
    LEFT JOIN sys_code b ON b.code_id = a.host_id AND b.code_type = "host_type"
    LEFT JOIN projects c ON c.project_id = a.host_project
    WHERE 1=1
    %s
    """ %(sql_fragment)

    #data = mysql_sql_exec(sql, sql_parameter)
    sqla = Sqla(current_app)
    data = sqla.fetch_to_dict(sql, sql_parameter)

    sql_total = """
    SELECT found_rows() as total 
    """
    #total = mysql_sql_exec(sql_total)
    total = sqla.fetch_to_dict(sql_total)[0]


    return (data, total['total'])


def host_info_query(host_id):
    sqla = Sqla(current_app)
    sql = """
    SELECT * FROM  host_instance a
    LEFT JOIN host_users b ON b.host_id = a.host_id AND b.user_role = "root"
    WHERE a.host_id = :host_id
    """
    host_user_info = sqla.fetch_to_dict(sql, {'host_id':host_id})
    if host_user_info:
        host_user_info = host_user_info[0]
    host_user_info['user_pass'] = sqla.sql_decrypt(host_user_info['user_pass'])

    info_obj = ServerInfo()
    info_obj.set_info(host_user_info)
    info_obj.connect()
    data = {**info_obj.get_freeinfo(), **info_obj.get_updateinfo()}
    info_obj.close()

    return data