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

    def start(self, func, param_list):
        if len(param_list) == 0:
            # logger.debug('提交到线程池的任务为空！')
            return False

        result = []
        for param in param_list:
            try:
                result.append(self.pool.apply_async(func=func, args=(param)))
            except Exception as e:
                print(e)
        self.pool.close()
        self.pool.join()

        # logger.debug('线程池内任务完成!回收线程！')
        # self.stop()
        return True




def test(test,test2):
    print ('参数1:%s,参数2:%s' %(test,test2))

if __name__ == '__main__':
    testp = ProcessPool()
    testp.start(test,[['00','11']])