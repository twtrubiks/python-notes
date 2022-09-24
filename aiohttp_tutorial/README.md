# AIOHTTP

Asynchronous HTTP Client/Server for asyncio and Python.

簡單說, aiohttp 就是非同步版的 requests,

而且 aiohttp 也可以搭配 [asyico_tutorial](https://github.com/twtrubiks/python-notes/tree/master/asyico_tutorial) 使用.

## 教學

在開始介紹之前, 非常推薦大家先讀一下官方文件的這篇

[The aiohttp Request Lifecycle](https://docs.aiohttp.org/en/latest/http_request_lifecycle.html)

簡單說一下, 一般使用 requests, 都是像以下這樣使用,

```python
response = requests.get('http://python.org')
print(response.text)
```

這雖然簡單, 但這卻不是最正確的使用方式,

更好的使用方式 [demo_request_session.py](https://github.com/twtrubiks/python-notes/blob/master/aiohttp_tutorial/demo_request_session.py)

```python
with requests.Session() as session:
    response = session.get('http://python.org')
    print(response.text)
```

在對一個網站發起請求時, 最好可以維護一個 session,

這樣可以降低握手次數, 就算是單線程, 效能也比較好.

安裝指令

```cmd
pip install aiohttp
```

一個很基本的 aiohttp 範例 [demo_aiohttp.py](https://github.com/twtrubiks/python-notes/blob/master/aiohttp_tutorial/demo_aiohttp.py),

和一般的 requests 相比, aiohttp 速度提昇不少(主要還是因為非同步的關係).

也可以搭配 timeout 使用, 可參考 [demo_aiohttp_client_timeout.py](https://github.com/twtrubiks/python-notes/blob/master/aiohttp_tutorial/demo_aiohttp_client_timeout.py)

可以透過 Semaphore 去調整併發的數量 [demo_aiohttp_semaphore.py](https://github.com/twtrubiks/python-notes/blob/master/aiohttp_tutorial/demo_aiohttp_semaphore.py)

## 執行環境

* Python 3.8

## Reference

* [https://docs.aiohttp.org/en/latest/index.html](https://docs.aiohttp.org/en/latest/index.html)
