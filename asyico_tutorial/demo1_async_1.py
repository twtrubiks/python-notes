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
    # Python 3.11 之前可以直接把 coroutine 丟給 asyncio.wait()
    # tasks = [something(i) for i in range(5)]
    # asyncio.run(asyncio.wait(tasks))

    # Python 3.11 起 asyncio.wait() 只接受 task, 而 task 必須在 event loop 中建立,
    # 所以透過 asyncio.Runner() 取得 event loop 再建立 task
    # (比較簡單的寫法是把 main() 抽出來, 請參考 demo1_async_2.py)
    with asyncio.Runner() as runner:
        tasks = [runner.get_loop().create_task(something(i)) for i in range(5)]
        runner.run(asyncio.wait(tasks))
    print('TIME: ', time.time() - start)

