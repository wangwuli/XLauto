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
    host_type = db.Column(db.String(50), nullable=False)
    host_project = db.Column(db.String(50))
    is_remove = db.Column(db.Integer, server_default=db.FetchedValue(), info='1为删除')
    comment = db.Column(db.String(50))



class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50))
    project_code = db.Column(db.String(50), info='项目编码')
    controller_ip = db.Column(db.String(50), info='项目区域子控制器')
    order_id = db.Column(db.Integer, info='查询排序')
    is_remove = db.Column(db.Integer, server_default=db.FetchedValue(), info='1为删除标记')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    modify_time = db.Column(db.DateTime, server_default=db.FetchedValue())
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
    is_remove = db.Column(db.Integer, server_default=db.FetchedValue(), info='1为删除')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    modify_time = db.Column(db.DateTime, server_default=db.FetchedValue())
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

    menu_id = db.Column(db.Integer, primary_key=True)
    menu_pid = db.Column(db.Integer)
    menu_name = db.Column(db.String(50))
    menu_url = db.Column(db.String(50))
    menu_icon = db.Column(db.String(50))
    statu = db.Column(db.Integer, server_default=db.FetchedValue(), info='0为禁用')
    comments = db.Column(db.String(50))
