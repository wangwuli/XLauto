from src.general.Sqla import Sqla
from flask import current_app


def get_hotst_connect_info(host_id):
    sqla = Sqla(current_app)
    sql = """
    SELECT * FROM  host_instance a
    LEFT JOIN host_users b ON b.host_id = a.host_id AND b.user_role = "root"
    WHERE a.host_id = :host_id
    """
    host_user_info = sqla.fetch_to_dict(sql, {'host_id' :host_id})
    if host_user_info:
        host_user_info = host_user_info[0]
    host_user_info['user_pass'] = sqla.sql_decrypt(host_user_info['user_pass'])

    return host_user_info