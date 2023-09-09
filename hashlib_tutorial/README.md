## hashlib

簡單說, 可以把它當成簡單的加密(簽名):smile:

### SHA-1

範例

```python
import hashlib

s = hashlib.sha1()
data = "twtrubiks"
s.update(data.encode('utf-8'))
h = s.hexdigest()
print(h)
```

來做一個應用, 如何偵測檔案是否有改動過:question:

可以直接讀取檔案內容, 並且 hash 內容,

然後把它保存起來, 下次再 hash 檔案內容一次,

只要 hash 出來的值和上次不一樣,

就代表檔案有被改動過, 範例如下

```python
import hashlib, os

s = hashlib.sha1()
file_name = 'detect_data.txt'
root_path = '<Your Path>'
s.update(file_name.encode('utf-8'))

with open(os.path.join(root_path, file_name), 'rb') as f:
    s.update(f.read())

h = s.hexdigest()
print(h)
```

### MD5

來個 MD5 簽名範例, 簽名規則,

先依照字典 key 排序, 接著組合成以下的字串,

`a=value1&b=value2&c=value3....key=secret_key`

將字串轉為大寫後, 再 MD5

```python
import hashlib
import time

Secret_Key = 'Secret_Key'

my_dict = {
    'name': 'twtrubiks',
    'age': '33',
    'sex': 'male',
    'time': int(time.time())
}

wait_to_signed = '&'.join([f'{key}={value}'for key, value in sorted(my_dict.items())])

str_to_signed = f'{wait_to_signed}&=key{Secret_Key}'.upper()
# print(str_to_signed)

# 開始簽名
md5_obj = hashlib.md5()
md5_obj.update(str_to_signed.encode())
print(md5_obj.hexdigest())
```