import asyncio
import time


async def a():
    print("Suspending a")
    await asyncio.sleep(1)
    # raise Exception('error')


async def b():
    print("Suspending b")
    await asyncio.sleep(2)
    print("Resuming b")
    return "B"


async def main():
    done, pending = await asyncio.wait(
        [a(), b()], return_when=asyncio.tasks.ALL_COMPLETED
    )
    print("done:", done)
    print("pending:", pending)


start = time.time()
asyncio.run(main())
print("TIME: ", time.time() - start)
