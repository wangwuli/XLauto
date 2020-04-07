#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
离线脚本
"""
from main import create_app
from main.models.models import db

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()