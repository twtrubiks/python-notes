"""
https://pypi.org/project/pycryptodome/

pip install pycryptodome

產生
public key 公鑰
private key 私鑰
"""

from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)

def generate_pem_key():
    # 產生 PEM 格式
    # PEM 使用 Base64 編碼
    private_key = rsa.export_key()
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    public_key = rsa.publickey().export_key()
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)

def generate_der_key():
    # 產生 DER 格式
    # DER 使用的是 二進位格式資料 (Binary encoding)
    private_key = rsa.export_key(format="DER")
    with open('private_key.der', 'wb') as f:
        f.write(private_key)

    public_key = rsa.publickey().export_key(format="DER")
    with open('public_key.der', 'wb') as f:
        f.write(public_key)

generate_pem_key()
# generate_der_key()