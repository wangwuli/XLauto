#!/usr/bin/env python

from main import create_app
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

if __name__ == '__main__':
    # from flask_script import Manager
    # manager = Manager(create_app())
    # manager.run()
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), create_app(), handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()