# dj-database-url-tutorial

簡單介紹一個套件， 名稱為 [dj-database-url](https://github.com/kennethreitz/dj-database-url)，

主要功能：**簡化 django db 連線字串設定**。

詳細的大家可以自行前往閱讀，這邊會筆記一些重點，

安裝套件

> pip install dj-database-url

使用方法很簡單，可參考 [settings.py](xxx)

```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))
}
```

註解的部份是原來的寫法，其他資料庫的連接方式請參考 [dj-database-url](https://github.com/kennethreitz/dj-database-url)。

## 執行環境

* Python 3.4.3