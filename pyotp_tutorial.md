## pyopt 教學

實作 two-factor (2FA) or multi-factor (MFA) authentication methods

安裝指令

```cmd
pip install pyotp
```

官方文件可參考 [pyotp](https://pypi.org/project/pyotp/)

這邊需要知道一次事情,OTP 產生的密碼是用時間和演算法完成的, 和網路沒關係,

所以有時候在使用的時候要注意 server 的時間有沒有跑掉, 不然會不準.

先產生一組 key

```python
import pyotp
import time
my_key = pyotp.random_base32()
print(my_key)
```

接著產生 QRCODE

```python
qrcode_uri = pyotp.totp.TOTP(my_key).provisioning_uri(\
    name='Test@test.com', issuer_name='TEST App')
print(qrcode_uri)

# otpauth://totp/TEST%20App:Test%40test.com?secret=7VOXCMNJYHKWZEPU5RSCBDT3VHBDHKAI&issuer=TEST%20App
```

注意, 這組字串也相當你的 key 不要亂丟給別人.

你會得到一串字串, 請把這串字串用任何工具轉成 QECODE (選擇 文字)

接著安裝 FreeOTP App or Google Authenticator,

然後掃秒 QECODE, 就會成功加入

基本上, 這邊印出的數字, 會和手機一模一樣

```python
totp = pyotp.TOTP(my_key)
print(totp.now())
```

如果你想樣驗證是否現在的 code 是有效的, 可以這樣用

```python
print(totp.verify('587597'))
```

看完上面的例子, 要注意一些事情, 首先, 每個帳號應該要有自己獨立的secret key,

每個 key 都用於單獨產生 一次性密碼 OTP, 這樣才能確保獨立性以及安全性.

因為假如多個帳號共用相同的 key, 這樣只要一個帳號的 key 外洩, 就全部完蛋了.

