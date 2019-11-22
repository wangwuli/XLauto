# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: logio.py
@time: 2019/11/22 17:10
@desc:
'''
from flask import Flask, escape, request
app = Flask(__name__)


def login():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

    # form = LoginForm()
    # if form.validate_on_submit():
    #     login_user(user)
    #     flask.flash('Logged in successfully.')
    #     next = flask.request.args.get('next')
    #     if not is_safe_url(next):
    #         return flask.abort(400)
    #     return flask.redirect(next or flask.url_for('index'))
#return flask.render_template('login.html', form=form)