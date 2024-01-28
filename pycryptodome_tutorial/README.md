# pycryptodome

RSA 非對稱加密, 會有兩把密鑰. 速度比較慢.

注意, RSA 簽名 和 RSA 加密 概念是不一樣的.

加密: 公鑰加密, 私鑰解密

簽名: 私鑰簽名, 公鑰驗簽

RSA 簽名 : 私鑰簽名, 公鑰驗簽

如果使用相同的 key 簽名 相同的字串, 每次結果都是**相同的**.

```python
# 產生 公鑰 私鑰 ( PEM or DER )
python3 generator_public_private_key.py

# 測試 私鑰簽名, 公鑰驗簽
python3 sign_and_verify_sign.py

# base64 編碼的 public key 和 private_key
# 需要先進行 b64decode
python3 base64_str_key_to_sign.py
```

RSA加解密 公鑰加密, 私鑰解密

如果使用相同的 key 加密 相同的字串, 每次結果都是**不相同的**.

```python
# RSA 加解密, 有最大加密長度限制
python3 rsa_encrypt_decrypted.py

# RSA 分段加解密
python3 rsa_segments_encrypt_decrypted.py
```

AES CBC 加解密

AES 對稱加密, 一把密鑰進行加密和解密. 速度比較快.

```python
python3 aes_tutorial
```