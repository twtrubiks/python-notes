# pyenv 教學

之前介紹過建立虛擬環境

[如何使用 venv 建立 virtual environments 📝](https://github.com/twtrubiks/python-creation-of-virtual-environments)

但最近發現 pyenv,

使用起來感覺更上手, 這邊簡單介紹一下

[https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

安裝方法

[Automatic installer](https://github.com/pyenv/pyenv#automatic-installer)

```cmd
curl https://pyenv.run | bash
```

安裝完應該會出現

![alt tag](https://i.imgur.com/z016ANU.png)

然後我是使用 zsh (所以跟著底下設定)

[Set up your shell environment for Pyenv](https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv)

```cmd
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

接著重開 zsh 輸入 `pyenv` 就不會跳出任何錯誤訊息了

# 教學

先看一下支援的版本

```cmd
pyenv install --list
```

這邊選擇 `3.9.18`, 所以先安裝 python 版本

```cmd
pyenv install 3.9.18
```

如果你在安裝環境的時候, 出現一些錯誤,

就是去把對應的安裝起來即可, 像是我安裝了這些

```cmd
sudo apt install lzma liblzma-dev python3-tk tk-dev libsqlite3-dev
```

接著建立環境

```cmd
pyenv virtualenv 3.9.18 test_env
```

啟動你的環境
```cmd
pyenv activate test_env
```

顯示全部安裝的 venv

```cmd
pyenv virtualenvs
```

也會顯示安裝的路徑

![alt tag](https://i.imgur.com/uFuL1CY.png)


刪除一個 venv

```cmd
pyenv uninstall test_env
```

## Reference

* [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

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