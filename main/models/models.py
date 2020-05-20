# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class HostInstance(db.Model):
    __tablename__ = 'host_instance'

    host_id = db.Column(db.Integer, primary_key=True)
    host_ip = db.Column(db.String(50), nullable=False)
    host_name = db.Column(db.String(50))
    host_port = db.Column(db.Integer)
    host_type_key = db.Column(db.String(50), nullable=False)
    host_project = db.Column(db.String(50))
    is_remove = db.Column(db.Integer)
    comment = db.Column(db.String(50))



class HostUser(db.Model):
    __tablename__ = 'host_users'

    user_id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_pass = db.Column(db.String(50), nullable=False)
    user_role = db.Column(db.String(50), nullable=False)



class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50))
    project_code = db.Column(db.String(50))
    controller_ip = db.Column(db.String(50))
    order_id = db.Column(db.Integer)
    is_remove = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    comments = db.Column(db.String(500))



class ScriptFileCabinet(db.Model):
    __tablename__ = 'script_file_cabinet'

    script_file_id = db.Column(db.Integer, primary_key=True)
    script_file_path = db.Column(db.String(300))
    script_file_name = db.Column(db.String(50))
    script_file_group = db.Column(db.String(50))
    script_file_type = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    modify_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    comment = db.Column(db.String(50))



class ScriptFileExecuteEvent(db.Model):
    __tablename__ = 'script_file_execute_event'

    script_file_execute_event_id = db.Column(db.Integer, primary_key=True)
    script_execute_event_batch_id = db.Column(db.Integer)
    script_file_id = db.Column(db.Integer)
    execute_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    execute_end_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    execute_result = db.Column(db.Integer, info='1为成功，0为失败')



class ServerSoftware(db.Model):
    __tablename__ = 'server_software'

    soft_id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, index=True)
    soft_type = db.Column(db.String(50), index=True)
    soft_port = db.Column(db.Integer)
    start_soft_cmd = db.Column(db.String(50))
    stop_soft_cmd = db.Column(db.String(50))
    restart_soft_cmd = db.Column(db.String(50))
    soft_log_path = db.Column(db.String(50))
    is_remove = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    modify_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    comments = db.Column(db.String(50))



class SysCode(db.Model):
    __tablename__ = 'sys_code'

    code_id = db.Column(db.Integer, primary_key=True)
    code_key = db.Column(db.String(50))
    code_name = db.Column(db.String(50), nullable=False)
    code_type = db.Column(db.String(50), nullable=False)
    f_code = db.Column(db.String(50))
    order_queue = db.Column(db.SmallInteger)
    comments = db.Column(db.String(50))



class SysMenu(db.Model):
    __tablename__ = 'sys_menu'

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    title = db.Column(db.String(50))
    name = db.Column(db.String(50))
    path = db.Column(db.String(50))
    icon = db.Column(db.String(50))
    statu = db.Column(db.Integer)
    comments = db.Column(db.String(50))
