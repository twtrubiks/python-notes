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

private_key = rsa.export_key()
with open('private_key.pem', 'wb') as f:
    f.write(private_key)

public_key = rsa.publickey().export_key()
with open('public_key.pem', 'wb') as f:
    f.write(public_key)
