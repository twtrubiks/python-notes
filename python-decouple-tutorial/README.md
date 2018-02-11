# python-decouple-tutorial

簡單介紹一個套件， 名稱為 [python-decouple](https://github.com/henriquebastos/python-decouple)，

主要功能：**強大的設定檔 library**。

詳細的大家可以自行前往閱讀，這邊會筆記一些重點，

安裝套件

> pip install python-decouple

設定檔可以是 `ini` file 或是 `env` file

`ini` file，檔名請命名為 `settings.ini`

```ini
[settings]
DEBUG=True
TEMPLATE_DEBUG=%(DEBUG)s
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
PERCENTILE=90%%
```

`env` file，檔名請命名為 `.env`

```env
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
PERCENTILE=90%
#COMMENTED=42
```

Decouple 選擇的順序如下

1. 環境變數 ( Environment variables )，第一順位。

2. 尋找是否有 `settings.ini` or `.env` file，第二順位。

3. config 通過參數設定的 default 值，第三順位。

這邊使用一個簡單的範例，可參考 [tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/python-decouple-tutorial/tutorial.py)

```python
from decouple import config

if __name__ == "__main__":
    DEBUG = config('DEBUG', default=False, cast=bool)
    print('DEBUG', DEBUG)
    '''
    environment variables have precedence over config files.
    os.environ['PATH'] = '/my_path'
    '''
    PATH = config('PATH', cast=str)
    print('PATH', PATH)
```

透過上面這個範例，看到 `cast` 這個設定的參數，這個參數可以設定型態，舉上面這個例子，

代表 DEBUG 將得到一個 bool，而不會像環境變數的方式回傳字串的 'False' （環境變數只能回傳字串）。

通常 [settings.ini](https://github.com/twtrubiks/python-notes/blob/master/python-decouple-tutorial/settings.ini) 這個檔案不會上 github ，也就是會被寫在 `.gitignore` 中，避免將敏感資料放到雲端 ，

有時候會放一個 `settings.example.ini` 上 github，需要的人再自行改檔名以及將內容的資訊換成正確的。

假如我佈署到 [heroku](https://www.heroku.com/)，這時候並不會有 [settings.ini](https://github.com/twtrubiks/python-notes/blob/master/python-decouple-tutorial/settings.ini)，我們就必須到網頁後台設定環境變數。

## 執行環境

* Python 3.4.3