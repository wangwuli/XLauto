# -*- coding: utf-8 -*-
'''
@author: liww
@file: course_test.py
@time: 2020/8/11 17:01
@desc:
'''
import multiprocessing


class ProcessPool():
    def __init__(self):
        # logger.debug('初始化池，线程数：%s' % (max_thread))
        self.pool = multiprocessing.Pool(processes=4)

    def start(self, func, param_list, wait=True):
        if len(param_list) == 0:
            # logger.debug('提交到线程池的任务为空！')
            return False

        result = []
        for param in param_list:
            result.append(self.pool.apply_async(func=func, args=(param,)))

        self.pool.close()
        self.pool.join()

        # logger.debug('线程池内任务完成!回收线程！')
        # self.stop()
        return True
