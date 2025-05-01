# pyenv 教學

之前介紹過建立虛擬環境

[如何使用 venv 建立 virtual environments 📝](https://github.com/twtrubiks/python-creation-of-virtual-environments)

但最近發現 pyenv(可以管理多版本),

使用起來感覺更上手, 這邊簡單介紹一下

[https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

安裝方法

[Automatic installer](https://github.com/pyenv/pyenv?tab=readme-ov-file#linuxunix)

```cmd
curl -fsSL https://pyenv.run | bash
```

安裝完應該會出現

![alt tag](https://i.imgur.com/z016ANU.png)

然後我是使用 zsh (所以跟著底下設定)

[Set up your shell environment for Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#zsh)

```cmd
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
```

接著重開 zsh 輸入 `pyenv` 就不會跳出任何錯誤訊息了

# 教學

先看一下支援的版本

```cmd
pyenv install --list
```

這邊選擇 `3.12.3`, 所以先安裝 python 版本

```cmd
pyenv install 3.12.3
```

查看目前全部已經安裝的 python 版本

```cmd
pyenv versions
```

如果想要移除安裝的 python 版本

```cmd
pyenv uninstall 3.12.0
```

💢 開始建立環境前,

請先安裝這個 [Suggested build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

不然很容易再建立的時候出錯誤,

以下為 Ubuntu/Debian/Mint 的環境,

```cmd
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

接著建立環境

```cmd
pyenv virtualenv 3.12.3 test_env
```

啟動你的環境

```cmd
pyenv activate test_env
```

生效作用範圍有 `shell` > `local` > `global` 可以使用 (可參考 [understanding-python-version-selection](https://github.com/pyenv/pyenv?tab=readme-ov-file#understanding-python-version-selection))

在目前的 shell 生效, 退出就消失了

```cmd
pyenv shell <version>
```

如果你想搭配 vscode 使用, 直接使用這個方法會比較快.

執行後目錄會多出 `.python-version` 這個檔案 (在當前的資料夾底下生效),

```cmd
pyenv local <version> -- automatically select whenever you are in the current directory (or its subdirectories),
```

在整個 user 底下都生效(全局改變),

如果要還原(切換)可以使用 `pyenv global system`

```cmd
pyenv global <version> -- select globally for your user account
```

顯示全部安裝的 venv

```cmd
pyenv virtualenvs
```

也會顯示安裝的路徑

![alt tag](https://i.imgur.com/uFuL1CY.png)

如果想查詢目前的 command 在哪個路徑下, 可使用以下指令

```cmd
❯ pyenv which pip3
/home/twtrubiks/.pyenv/versions/3.10.13/bin/pip3
❯ pyenv which python3
/home/twtrubiks/.pyenv/versions/3.10.13/bin/python3
```

刪除一個 venv

```cmd
pyenv virtualenv-delete test_env
```

## Reference

* [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡 :laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](http://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license