## marshmallow

文件 [https://marshmallow.readthedocs.io/en/stable/](https://marshmallow.readthedocs.io/en/stable/)


安裝套件

```python
pip install -U marshmallow
```

- 反序列化 (Loading)

```txt
Deserialize input data to app-level objects.
The reverse of the dump method is load,
which validates and deserializes an input dictionary to an application-level data structure
```

- 序列化 (Dumping) obj -> dict

```txt
Serialize app-level objects to primitive Python types.
The serialized objects can then be rendered to standard formats
such as JSON for use in an HTTP API.
```

範例 [demo.py](https://github.com/twtrubiks/python-notes/blob/master/marshmallow_tutorial/demo.py)

```python
python3 demo.py
```

讀取 json 並且驗證資料 [validating_package.py](https://github.com/twtrubiks/python-notes/blob/master/marshmallow_tutorial/validating_package.py)

[package_correct.json](package_correct.json)

[package_error.json](package_error.json)

```python
python3 validating_package.py
```

更多例子 [https://marshmallow.readthedocs.io/en/stable/examples.html](https://marshmallow.readthedocs.io/en/stable/examples.html)
