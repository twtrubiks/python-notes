import asyncio

async def nested():
    return 42

background_tasks = set()

def task_cb(context):
    print("Task completion received...")
    print("Name of the task:%s"%context.get_name())
    # print("Wrapped coroutine object:%s"%context.get_coro())
    print("Task is done:%s"%context.done())
    print("Task has been cancelled:%s"%context.cancelled())
    print("Task result:%s"%context.result())

    print(context)
    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    background_tasks.discard(context)

async def main():
    for _ in range(10):
        task = asyncio.create_task(nested())

        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)
        # https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.add_done_callback
        task.add_done_callback(task_cb)

asyncio.run(main())