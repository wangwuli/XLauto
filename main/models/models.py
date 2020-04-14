# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class HostInstance(db.Model):
    __tablename__ = 'host_instance'

    host_id = db.Column(db.Integer, primary_key=True)
    host_ip = db.Column(db.String(50), nullable=False)
    host_name = db.Column(db.String(50))
    host_type = db.Column(db.String(50), nullable=False)
    host_project = db.Column(db.String(50))
    is_remove = db.Column(db.Integer)
    comment = db.Column(db.String(50))



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
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    comments = db.Column(db.String(50))



class SysCode(db.Model):
    __tablename__ = 'sys_code'

    code_id = db.Column(db.Integer, primary_key=True)
    code_key = db.Column(db.String(50), nullable=False)
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
