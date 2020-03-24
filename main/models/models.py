# coding: utf-8
from sqlalchemy import Column, Integer, SmallInteger, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class HostInstance(db.Model):
    __tablename__ = 'host_instance'

    id = db.Column(db.Integer, primary_key=True)
    host_ip = db.Column(db.String(50), server_default=db.FetchedValue())
    host_type = db.Column(db.String(50), server_default=db.FetchedValue())
    host_project = db.Column(db.String(50), server_default=db.FetchedValue())
    comment = db.Column(db.String(50), server_default=db.FetchedValue())



class SysCode(db.Model):
    __tablename__ = 'sys_code'

    id = db.Column(db.Integer, primary_key=True)
    code_key = db.Column(db.String(50), nullable=False)
    code_name = db.Column(db.String(50), nullable=False)
    code_type = db.Column(db.String(50), nullable=False)
    f_code = db.Column(db.String(50), nullable=False)
    order_queue = db.Column(db.SmallInteger, nullable=False)
    comments = db.Column(db.String(50), nullable=False)
