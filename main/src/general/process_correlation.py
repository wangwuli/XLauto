# -*- coding: utf-8 -*-
'''
@author: liww
@file: process_correlation.py
@time: 2020/8/11 14:49
@desc:
'''
import asyncio
import multiprocessing

from flask import current_app
import psutil


# async def xlauto_threadpool():
#     pool_number = current_app.config['POOL_ALLOW_NUMBER'] if current_app.config[
#         'POOL_ALLOW_NUMBER'] else psutil.cpu_count()
#
#     semaphore = asyncio.Semaphore(int(pool_number))  # 限制并发量
#
#     current_app.xlaoto_loop = asyncio.get_event_loop()

class ProcessPool():
    def __init__(self):
        pool_number = current_app.config['POOL_ALLOW_NUMBER'] if current_app.config[
            'POOL_ALLOW_NUMBER'] else psutil.cpu_count()
        # multiprocessing.set_start_method('fork')
        self.pool = multiprocessing.Pool(processes=pool_number)

    # def log_record(self, e):
    #     xlauto = current_app._get_current_object()
    #     xlauto.logger.info(e)

    def start(self, func, param_list):
        if len(param_list) == 0:
            return False
        result = []

        for param in param_list:
            # result.append(self.pool.apply_async(func=func, args=(param), callback=self.log_record))
            result.append(self.pool.apply_async(func=func, args=(param)))

        self.pool.close()
        self.pool.join()

        return True