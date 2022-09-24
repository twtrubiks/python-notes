"""
https://docs.python.org/3/library/asyncio.html
asyncio is often a perfect fit for IO-bound and high-level structured network code.
"""

import asyncio
import time

# def 前面加上 async 就會變成 coroutine function (有非同步的功能)
async def something(num):
    print('第 {} 任務，第一步'.format(num))
    # time.sleep is blocking call.
    # Hence, it cannot be awaited and we have to use asyncio.sleep
    # await 就是用來暫停或繼續的點, 其實它背後就是用 yield 實做的
    await asyncio.sleep(2)
    print('第 {} 任務，第二步'.format(num))

if __name__ == "__main__":
    start = time.time()
    tasks = [something(i) for i in range(5)]
    asyncio.run(asyncio.wait(tasks))
    print('TIME: ', time.time() - start)

