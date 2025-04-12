# thread and process

Concurrency 併發, 可以看做是 Thread (I/O-bound)

當我們需要等待的時候(像是等待網路上的 response), 這時候我們可以先去做別的事情.

![alt tag](https://i.imgur.com/UgSkv1R.png)

Parallelism 並行, 可以看做是 Process (CPU-bound)

一次開很多個人同時完成, 就像是大量的影分身.

![alt tag](https://i.imgur.com/mVhT1qO.png)

[圖片來源 slide](https://go.dev/talks/2012/waza.slide)

## thread

主要使用在 I/O bound, 像是爬蟲或寫資料這種需要等待的類型.

### join

執行 [demo_threading_non_join.py](demo_threading_non_join.py)

你會發現輸出如下

```cmd
> python3 demo_threading_non_join.py

開始執行 1
開始執行 2
開始執行 3
main thread quit
結束 3
結束 1
結束 2
```

還沒有執行結束, 就執行了 main thread quit.

如果執行 [demo_threading_join.py](demo_threading_join.py)

```cmd
> python3 demo_threading_join.py

開始執行 1
開始執行 2
開始執行 3
結束 2
結束 3
結束 1
main thread quit
```

當加入 join, 程式就會等到全部執行完才接著往下執行,

可以看到 main thread quit 顯示在最後.

### daemon

當主要的 thread 退出的時候, 你會發現 `main()` 持續在執行,

除非你 `ctrl+c` 才會中斷,

執行 [demo_threading_non_daemon.py](demo_threading_non_daemon.py)

```cmd
> python3 demo_threading_non_daemon.py

執行中...
isDaemon: False
執行中...
執行中...
執行中...
執行中...
執行中...
main thread quit
執行中...
執行中...
......
```

當我們使用 daemon 就不一樣了, 當主要的 thread 退出的時候,

整個 thread 就會被停止了

執行 [demo_threading_daemon.py](demo_threading_daemon.py)

```python
> python3 demo_threading_daemon.py

daemon Thread
執行中...
isDaemon: True
執行中...
執行中...
執行中...
執行中...
main thread quit
```

這邊再給一個範例, 利用 daemon 持續更新或監控某件事情

```python
import threading
import time

def keep_updates():
    """
    保持更新
    """
    print('run keep_updates')
    count = 0
    while True:
        try:
            count += 1
            # do somethings......
            print(count)
            time.sleep(0.5)
        except Exception:
            print('Exception')
            time.sleep(10)

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=keep_updates, daemon=True)
    monitor_thread.start()

    # 等待主 thread 結束, 避免退出
    monitor_thread.join()
```

### lock

當同時有很多個 Thread 要用到同一個資料時，

為了不發生 Race Condition 的現象，

需要使用 `lock.acquire()` 以及 `lock.release()` 來將它鎖定,

不要讓其他 Thread 執行.

先來看一個 Race Condition 的例子,

兩個 thread 分別加減 3, 多執行幾次,

有時後會出現很奇怪的現象(如下), 這就是戶搶的結果.

執行 [demo_threading_non_lock.py](demo_threading_non_lock.py)

```cmd
> python3 demo_threading_non_lock.py

This is the first thread  1
This is the second thread  0
This is the second thread  0
This is the first thread  1
This is the second thread  0
This is the first thread  1
```

透過 lock 改善這段 code,

不管執行幾次, 結果永遠是正確的輸出,

執行 [demo_threading_lock.py](demo_threading_lock.py)

```cmd
> python3 demo_threading_lock.py

This is the first thread  1
This is the first thread  2
This is the first thread  3
This is the second thread  2
This is the second thread  1
This is the second thread  0
```

## process

主要使用在 CPU bound, 大量使用 CPU 的情境.

基本上, 使用上和 thread 大同小異.

### join

執行 [demo_process_non_join.py](demo_process_non_join.py),

你會發現輸出如下

```cmd
> python3 demo_process_non_join.py

開始執行 ['www.yahoo.com.tw, www.google.com']
main process quit
開始執行 ['www.yahoo.com.tw, www.google.com']
開始執行 ['www.yahoo.com.tw, www.google.com']
結束 1
結束 2
結束 3
```

還沒有執行結束, 就執行了 main process quit.

如果執行 [demo_process_join.py](demo_process_join.py)

```cmd
> python3 demo_process_join.py

開始執行 ['www.yahoo.com.tw, www.google.com']
開始執行 ['www.yahoo.com.tw, www.google.com']
開始執行 ['www.yahoo.com.tw, www.google.com']
結束 2
結束 1
結束 3
main process quit
```

當加入 join, 程式就會等到全部執行完才接著往下執行,

可以看到 main process quit 顯示在最後.

## 其他

一般除了看到 `import threading` `import multiprocessing` 之外,

還有更高階的套件, 就是 `concurrent.futures`,

請參考 [concurrent_futures_tutorial](https://github.com/twtrubiks/python-notes/tree/master/concurrent_futures_tutorial)

至於要使用 `import threading` `import multiprocessing`,

還是 `concurrent.futures` 這部份, 基本上都可以,

`concurrent.futures` 學習成本低一點 :smile:

( 相對 `import threading` `import multiprocessing` 來說, 細節比較少 ).

## 延伸閱讀

* [Asyncio](https://github.com/twtrubiks/python-notes/tree/master/asyico_tutorial)

## Reference

* [https://docs.python.org/3/library/threading.html](https://docs.python.org/3/library/threading.html)
* [https://docs.python.org/3/library/multiprocessing.html](https://docs.python.org/3/library/multiprocessing.html)
