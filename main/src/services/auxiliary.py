from src.general.Sql_G import mysql_sql_exec


def home_hosts_query_filter(parameter_dict):
    sql_fragment = ''
    sql_parameter = []
    if parameter_dict['host_project'] != '':
        sql_fragment += "AND a.host_project = %s "
        sql_parameter.append(parameter_dict['host_project'])

    if parameter_dict['host_type'] != '':
        sql_fragment += "AND a.host_type = %s "
        sql_parameter.append(parameter_dict['host_type'])

    if parameter_dict['host_ip'] != '':
        sql_fragment += "AND a.host_ip LIKE %s "
        sql_parameter.append('%%%s%%' %parameter_dict['host_ip'])


    sql = """
    SELECT a.host_id,a.host_ip,a.host_name,b.code_name AS host_type_text,c.project_name FROM host_instance a
    LEFT JOIN sys_code b ON b.code_id = a.host_id
    LEFT JOIN projects c ON c.project_id = a.host_project
    WHERE 1=1
    %s
    """ %(sql_fragment)

    return mysql_sql_exec(sql, sql_parameter)