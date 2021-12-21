# vcrpy 介紹教學 - 輕鬆把 request 錄下來

* [Youtube Tutorial - vcrpy 介紹教學 - 輕鬆把 request 錄下來](https://youtu.be/LrAxl5vfXJ4)

建議搭配影片服用:smile:

## 說明

常常在串接 api 的時候, 有時候對方的 api 很慢, 每測試一次就要等一下:sweat:

雖然我們可以直接把 response 的內容複製下來, 貼到文字檔的文件, 然後

再去讀那個文件檔, 這可能是一種方法, 但有沒有更好的方法呢:question:

當然有, 就是今天要介紹的 `vcrpy`:smile:

官方文件可參考 [https://vcrpy.readthedocs.io/en/latest/installation.html](https://vcrpy.readthedocs.io/en/latest/installation.html)

安裝方法 ( python 版本至少要 `Python 3.5+`)

```cmd
pip install vcrpy
```

使用方法也很簡單

```python
import vcr
import requests

@vcr.use_cassette('fixtures/vcr_cassettes/demo.yaml')
# @vcr.use_cassette()
def demo():
    response = requests.get('http://127.0.0.1:8000/api/image/test')
    data = response.json()
    print(data['id'], data['Url'])

demo()
```

第一次執行的時候, 會真的發出去 `request`, 並且會把資訊全部都錄下來,

並且保存在你所指定的路徑(也可以讓系統自動產生).

當你第二次執行時, 它會檢查是否有對應的 vcr_cassettes, 如果有的話,

就會直接讀取你錄下來的檔案(不會真的發出去 `request`).

但假如今天同一隻 api, 相同參數, server 端回應不同的資料給你, 這時候

你就只能刪掉錄下來的 vcr_cassettes, 重新錄一次即可.

這個 `vcrpy` 很方便, 推薦大家有空看看他的文件, 它也可以整合你的測試.