# -*- coding: utf-8 -*-
'''
@author: liww
@file: process_correlation.py
@time: 2020/8/11 14:49
@desc:
'''
import asyncio
from flask import current_app
import psutil


async def xlauto_threadpool():
    pool_number = current_app.config['POOL_ALLOW_NUMBER'] if current_app.config[
        'POOL_ALLOW_NUMBER'] else psutil.cpu_count()

    semaphore = asyncio.Semaphore(int(pool_number))  # 限制并发量

    current_app.xlaoto_loop = asyncio.get_event_loop()
