# -*- coding: utf-8 -*-

from . import services
from src.general.General import Result


@services.route('/home/menu_query', methods=['GET'])
def home_menu_query():
    data = [
        {
            "entity": {
                "id": 0,
                "name": "home",
                "icon": "el-icon-s-home",
                "title": "主页"
            }
        },
        {
            "entity": {
                "id": 1,
                "name": "instrument",
                "icon": "el-icon-s-cooperation",
                "title": "工具"
            },

            "childs": [
                {
                    "entity": {
                        "id": 3,
                        "name": "network",
                        "icon": "el-icon-place",
                        "title": "网络",
                        "path": "/network"
                    }
                },
                {
                    "entity": {
                        "id": 2,
                        "name": "test",
                        "icon": "el-icon-place",
                        "title": "主机",
                        "path": "/test"
                    }
                }
            ]
        },
        {
            "entity": {
                "id": 4,
                "name": "deploy",
                "icon": "el-icon-s-claim",
                "title": "部署"
            }
        },
        {
            "entity": {
                "id": 5,
                "name": "info_record",
                "icon": "el-icon-s-custom",
                "title": "维护"
            }
        },
    ]

    return Result.success_response(data,'菜单加载成功')


@services.route('/home/hosts_query', methods=['GET'])
def home_hosts_query():
    data = [{
        'ipaddr': '192.168.1.1',
        'app_name': 'Nginx',
        'use_name': '出口代理'
      }, {
        'ipaddr': '192.168.1.2',
        'app_name': 'Mysql',
        'use_name': '产品数据库'
      }]

    return Result.success_response(data,'目标主机加载成功')