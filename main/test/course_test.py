# -*- coding: utf-8 -*-
'''
@author: liww
@file: course_test.py
@time: 2020/8/11 17:01
@desc:
'''

import time
import asyncio


now = lambda : time.time()

start = now()
async def do_some_work(x):
    async with asyncio.Semaphore(1):
        for id in range(3):
            print("Time:", now() - start)
            await asyncio.sleep(1)
            print("waiting:", x)
            print("Time:", now() - start)


# 这里是一个协程对象，这个时候do_some_work函数并没有执行
coroutine = do_some_work(2)
coroutine2 = do_some_work(3)
#  创建一个事件loop
loop = asyncio.get_event_loop()

# 将协程加入到事件循环loop
tasks=[coroutine,coroutine2]
loop.run_until_complete(asyncio.wait(tasks))
asyncio.get_event_loop().run_forever()
time.sleep(10)
tasks2=[coroutine,coroutine2]
loop.run_until_complete(asyncio.wait(tasks2))

# loop.run_until_complete(asyncio.wait(coroutine2))
