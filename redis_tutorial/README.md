# redis 指令

這篇文章主要是紀錄一些 redis 指令,

很久前在 [django-docker-redis-tutorial 基本教學](https://github.com/twtrubiks/django-docker-redis-tutorial) 這篇文章有說明過,

但想要再寫一篇:smile:

附上 redis [docker-compose.yml](https://github.com/twtrubiks/python-notes/blob/master/redis_tutorial/docker-compose.yml)

也請記得安裝套件

```cmd
pip3 install redis
```

官方文件可參考 [https://github.com/redis/redis-py](https://github.com/redis/redis-py)

[redis_base.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_base.py)

如果中文亂碼, 可加上 `decode_responses=True`, cli 模式下可使用 `redis-cli --raw`.

[redis_lock_unlock.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_lock_unlock.py) - redis lock/unlock

[redis_mbase.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_mbase.py) - 一次設定/取得多個值.

[redis_msetnx.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_msetnx.py) - redis msetnx

[redis_ttl.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_ttl.py) - 設定 TTL

[redis_scan_iter.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_scan_iter.py) - redis scan_iter

[redis_list.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_list.py) - redis list

[redis_lpush_tutorial.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_lpush_tutorial.py) - simple MQ - redis lpush

[redis_brpop_tutorial.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_brpop_tutorial.py) - simple MQ - redis brpop

[redis_set.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_set.py) - redis set

[redis_sorted_set.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_sorted_set.py) - redis sorted set

[redis_hash.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_hash.py) - redis hash

[redis_pipeline.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_pipeline.py) - redis pipeline

[redis_pipeline_watch.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_pipeline_watch.py) - redis pipeline watch

[redis_json.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_json.py) - redis save json

[redis_pickle.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_pickle.py) - python object to pickle save redis (not recommended, use json)

[redis_object_class.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_object_class.py) - python object to json save redis (recommended)

[redis_stream.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_stream.py) - redis stream

## redis listen/pulish

[redis_listen.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_listen.py) - redis listen

[redis_pulish.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_pulish.py) - redis pulish

先執行 `python3 redis_listen.py` 保持監聽,

接著再執行 `python3 redis_pulish.py`, 前面的 terminal 會輸出訊息.

[redis_pub_sub.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_pub_sub.py) - redis_pub_sub example

## redis autocomplete

[redis_autocomplete.py](https://github.com/twtrubiks/python-notes/tree/master/redis_tutorial/redis_autocomplete.py)

## 其他

如果你不是用 docker 建立 redis, 是使用安裝在本機上的,

設定開機自動啟動 redis, 可以透過 [systemctl](https://github.com/twtrubiks/linux-note/tree/master/systemctl-tutorial),

```cmd
sudo systemctl enable redis-server
```
