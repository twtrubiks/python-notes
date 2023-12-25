"""
https://pypi.org/project/pycryptodome/

pip install pycryptodome

ref
https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(plaintext, key, iv):
    # AES.block_size -> 16
    encoded_padded = pad(plaintext.encode(), AES.block_size)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encoded = cipher.encrypt(encoded_padded)
    print(encoded)
    return encoded

def aes_decrypt(plaintext, key, iv):
    # AES.block_size -> 16
    decrypt_cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted = decrypt_cipher.decrypt(plaintext)
    decoded = unpad(decrypted, AES.block_size)
    print(decoded)# 必須為16位
    return decoded


plaintext = "hello world"
key = "key23X8Ib9LM8w16" # 必須為16位
iv = "iva23X8Ib9LM8w16" # 必須為16位

encode_data = aes_encrypt(plaintext, key, iv)
decoded_data = aes_decrypt(encode_data, key, iv)
