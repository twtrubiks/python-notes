# uv 教學

- [Youtube Tutorial - Streamlit 教學, 搭配 Pyenv, UV 高效開發](https://youtu.be/cH1pb_o7EPA)

官方文件 [uv](https://docs.astral.sh/uv/)

這個安裝套件真的非常快, 如果你一次安裝很多套件, 你就能了解他有多快.

安裝方法,

```cmd
curl -LsSf https://astral.sh/uv/install.sh | sh
```

或是你也可以用 `pip3 install uv` 安裝.

使用方法,

uv 支援 pip 安裝界面, [The pip interface](https://docs.astral.sh/uv/pip/#the-pip-interface)

```python
uv pip install ruff
```

如果要安裝 requirements.txt 一樣加上 uv 而已

```python
uv pip install -r requirements.txt
```

[Using tools](https://docs.astral.sh/uv/guides/tools/)

uvx 是一個工具, 它可以在不安裝套件的情況下(安裝在暫存區), 就使用這個套件做一些簡單的測試.

```cmd
uvx pycowsay hello from uv
```

uv 非常多功能, 也可以建立 venv,

但我自己主要是使用 [pyenv 教學](https://github.com/twtrubiks/python-notes/tree/master/pyenv_tutorial), 所以這邊就不再介紹, 有興趣的可以再到官網研究.