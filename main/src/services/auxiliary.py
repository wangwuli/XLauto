from src.general.Sql_G import mysql_sql_exec
from src.general.Sqla import Sqla
from flask import current_app


def home_hosts_query_filter(parameter_dict):

    sql_fragment = ''
    sql_parameter = []
    if parameter_dict['host_project'] != '':
        sql_fragment += "AND a.host_project = %s "
        sql_parameter.append(parameter_dict['host_project'])

    if parameter_dict['host_type'] != '':
        sql_fragment += "AND a.host_type_key = %s "
        sql_parameter.append(parameter_dict['host_type'])

    if parameter_dict['host_ip'] != '':
        sql_fragment += "AND a.host_ip LIKE %s "
        sql_parameter.append('%%%s%%' %parameter_dict['host_ip'])

    sql_fragment += "LIMIT %s,%s "
    size = int(parameter_dict["size"])
    page = int(parameter_dict["page"])
    start = (page - 1) * size
    sql_parameter.append(start)
    sql_parameter.append(size)


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
    total = sqla.fetch_to_dict(sql_total)


    return (data, total['total'])