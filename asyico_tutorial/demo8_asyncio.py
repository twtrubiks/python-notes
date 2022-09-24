# https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for

import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())