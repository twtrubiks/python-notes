## hashlib

簡單說, 可以把它當成簡單的加密:smile:

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