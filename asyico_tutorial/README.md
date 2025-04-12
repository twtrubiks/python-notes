# Asyncio

Use asyncio when you can, threading when you must.

Asyncio 適合 I/O-bound,

遇到 I/O-bound, 先考慮 Asyncio, 如果不適合再考慮 threading,

遇到 CPU-bound, 考慮 Process.

補充說明, Concurrency 併發 和 Parallelism 並行.

Concurrency 併發, 有同時處理多個任務的能力, 也是廣義的並行.

Parallelism 並行, 在同一時間執行多個操作, 而 Multi-processing 是一種實現並行性的方法.

Thread or Asyncio 可以認為是 Concurrency, 而 Process 可以當成 Parallelism.

## 教學

安裝指令

```cmd
pip install asyncio
```

先來看一個例子 [demo1_sync.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo1_sync.py)

這是一個同步的程式, 按照任務步驟一個一個執行, 總共需要10秒.

來看透過 asyncio 非同步(異步) 的 [demo1_async_1.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo1_async_1.py)

你會發現同樣的事情, 只需要2秒就執行完了 :exclamation: :exclamation:

但沒有像同步這樣按照順序一個一個執行(包含結果).

[demo1_async_2.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo1_async_2.py) 和 [demo1_async_1.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo1_async_1.py) 其實是一樣的,

差別只是有沒有把 `main()` 抽出來寫這樣而已.

接著來看一下程式碼,

```python
# def 前面加上 async 就會變成 coroutine function (有非同步的功能)
async def something(num):
    print('第 {} 任務，第一步'.format(num))
    # time.sleep is blocking call.
    # Hence, it cannot be awaited and we have to use asyncio.sleep
    # await 就是用來暫停或繼續的點, 其實它背後就是用 yield 實做的
    await asyncio.sleep(2)
    print('第 {} 任務，第二步'.format(num))
```

要寫 async 的程式只需要在前面加上 async, 這樣就可以了, 當你加上它,

就變成了所謂的 coroutine function (有非同步的功能).

而 `await` 這個地方就是可以暫停或繼續的點, 當有 IO-bound 需要等待的時候,

就先去執行其他的東西, 等收到事件後, 再回來執行, 至於它是如何做到暫停繼續的 :question:

背後就是透過 yield 實做的.

接下來我將透過官方文件的一些範例和大家簡單說明 Asyncio,

當執行 asyncio 的時候, 一定要用 `asyncio.run(...)` 把主程式包起來,

範例可參考 [demo2_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo2_asyncio.py)

當你執行 [demo3_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo3_asyncio.py) 的時候, 執行時間大約 3 秒, 你會發現根本沒有節省時間,

原因是因為你要把它使用 `asyncio.create_task(..)` 包起來,

像是 [demo4_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo4_asyncio.py), 這個範例執行時間就變成了 2 秒.

接著來看 [Awaitables](https://docs.python.org/3/library/asyncio-task.html#awaitables), 一個 coroutine object 記得要搭配 await 使用,

否則會跳出 `RuntimeWarning`, 可參考 [demo5_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo5_asyncio.py),

也可以透過 `asyncio.create_task(..)` 執行 coroutine function. 可參考 [demo6_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo6_asyncio.py),

如果希望在 task 完成後觸發某些事情, 可以透過 `add_done_callback()`, 可參考 [demo7_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo7_asyncio.py),

假如想設定 timeout, 可以使用 `asyncio.wait_for(...)`,

當 timeout 時會跳出 `asyncio.TimeoutError`, 可參考 [demo8_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo8_asyncio.py).

除了 `asyncio.create_task(..)`, 還有更 higher-level 的 `asyncio.gather(...)` 可以使用,

[Running Tasks Concurrently](https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)

可參考 [demo9_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo9_asyncio.py), 輸出結果會依照當初的順序(但還是非同步).

如果今天想知道細節, 像是任務是否 pending 之類的, 可以使用 `asyncio.wait(...)` 可參考 [demo10_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo10_asyncio.py).

除此之外, 當然還有 subprocess, 可參考 [demo11_asyncio.py](https://github.com/twtrubiks/python-notes/blob/master/asyico_tutorial/demo11_asyncio.py).

## 執行環境

* Python 3.8

## Reference

* [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)

* [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/#when-is-concurrency-useful)

* [AsyncIO, Threading, and Multiprocessing in Python](https://medium.com/analytics-vidhya/asyncio-threading-and-multiprocessing-in-python-4f5ff6ca75e8)