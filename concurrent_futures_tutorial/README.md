# concurrent.futures

除了之前介紹過的 [thread and process](https://github.com/twtrubiks/python-notes/tree/master/thread_process_tutorial) 之外,

還有更高階的套件可以使用, 就是 `concurrent.futures`

## ThreadPoolExecutor

主要使用在 I/O bound, 像是爬蟲或寫資料這種需要等待的類型.

### submit

執行 [demo_ThreadPoolExecutor_submit.py](demo_ThreadPoolExecutor_submit.py)

```cmd
python3 demo_ThreadPoolExecutor_submit.py
```

### map

透過迭代的方式

執行 [demo_ThreadPoolExecutor_map.py](demo_ThreadPoolExecutor_map.py)

```cmd
python3 demo_ThreadPoolExecutor_map.py
```

### lock

當同時有很多個 Thread 要用到同一個資料時，

為了不發生 Race Condition 的現象，

需要借用 Thread 裡面的 `threading.Lock()` 來防止其他 Thread 執行.

來看一個 RaceConditions 戶搶的狀況,

執行 [demo_ThreadPoolExecutor_RaceConditions.py](demo_ThreadPoolExecutor_RaceConditions.py)

```cmd
python3 demo_ThreadPoolExecutor_RaceConditions.py
```

你會發現有時候出現不是 2 的狀況, 只要出現的不是 2,

就是產生了 RaceConditions.

使用 lock, 執行 [demo_ThreadPoolExecutor_aviod_RaceConditions.py](demo_ThreadPoolExecutor_aviod_RaceConditions.py)

```cmd
python3 demo_ThreadPoolExecutor_aviod_RaceConditions.py
```

輸出永遠都是 2, 不會產生 RaceConditions.

## ProcessPoolExecutor

主要使用在 CPU bound, 大量使用 CPU 的情境.

基本上, 使用上和 ThreadPoolExecutor 大同小異,

就只是換成 ProcessPoolExecutor 即可.

### submit

執行 [demo_ProcessPoolExecutor_submit.py](demo_ProcessPoolExecutor_submit.py)

```cmd
python3 demo_ProcessPoolExecutor_submit.py
```

關於 `max_workers` 預設的說明, 官方文件有提到

```txt
Changed in version 3.8: Default value of max_workers is changed to min(32, os.cpu_count() + 4). This default value preserves at least 5 workers for I/O bound tasks. It utilizes at most 32 CPU cores for CPU bound tasks which release the GIL. And it avoids using very large resources implicitly on many-core machines.
```

### map

透過迭代的方式

執行 [demo_ProcessPoolExecutor_map.py](demo_ProcessPoolExecutor_map.py)

```cmd
python3 demo_ProcessPoolExecutor_map.py
```

關於 map 中的 chunksize, 文件說明如下

```txt
For very long iterables, using a large value for chunksize can significantly improve performance compared to the default size of 1. With ThreadPoolExecutor, chunksize has no effect.
```

## 延伸閱讀

* [Asyncio](https://github.com/twtrubiks/python-notes/tree/master/asyico_tutorial)

## Reference

* [https://docs.python.org/3/library/concurrent.futures.html](https://docs.python.org/3/library/concurrent.futures.html)