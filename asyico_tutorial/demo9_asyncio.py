import asyncio
import time

async def something(num):
    print('第 {} 任務，第一步'.format(num))
    await asyncio.sleep(2)
    print('第 {} 任務，第二步'.format(num))
    return '第 {} 任務完成'.format(num)

async def raise_error():
    1/0

async def main():
    tasks = [something(i) for i in range(5)]
    tasks1 = [raise_error() for _ in range(5)]

    # https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
    results = await asyncio.gather(*tasks, *tasks1, return_exceptions=True)
    print(results)


if __name__ == "__main__":

    start = time.time()
    asyncio.run(main())
    print("TIME:", time.time() - start)