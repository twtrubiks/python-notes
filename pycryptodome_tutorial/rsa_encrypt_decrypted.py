"""
https://pypi.org/project/pycryptodome/

pip install pycryptodome

RSA 加解密 公鑰加密, 私鑰解密
"""


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode


key = RSA.generate(2048)

public_key = key.publickey()
private_key = key

cipher = PKCS1_OAEP.new(public_key)
decipher = PKCS1_OAEP.new(private_key)

def encrypted(plaintext):
    # 公鑰加密
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    encrypted_msg = b64encode(ciphertext).decode('utf-8')
    print("Encrypted message:", encrypted_msg)
    return encrypted_msg

def decrypted(encrypted_msg):
    # 私鑰解密
    ciphertext = b64decode(encrypted_msg.encode('utf-8'))
    decrypted_message = decipher.decrypt(ciphertext)
    print("Decrypted message:", decrypted_message.decode('utf-8'))
    return decrypted_message.decode('utf-8')


plaintext = "Hello, World"
encrypted_msg = encrypted(plaintext)
decrypted(encrypted_msg)
