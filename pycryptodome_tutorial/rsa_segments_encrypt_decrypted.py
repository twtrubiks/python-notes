"""
https://pypi.org/project/pycryptodome/

pip install pycryptodome

RSA 加解密 公鑰加密, 私鑰解密 - 分段加解密

RSA 1024 加密最大長度為117 Byte, 解密最大長度為128 Byte
RSA 2048 加密最大長度為245 Byte, 解密最大長度為256 Byte

解決 ValueError: Plaintext is too long.
"""

import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode


key = RSA.generate(2048)

public_key = key.publickey()
private_key = key

cipher = PKCS1_OAEP.new(public_key)
decipher = PKCS1_OAEP.new(private_key)

def encrypted(plaintext):

    # 公鑰加密 - 分段加密
    # PKCS1 v1.5 的 padding 佔用 11 個 byte
    # OAEP 的 padding 佔用 42 個 byte
    max_encryptable_block_size = key.size_in_bytes() - 42

    msg = plaintext.encode('utf-8')
    length = len(msg)

    offset = 0
    ciphertext = ''.encode('utf-8')
    while length - offset > 0:
        if length - offset > max_encryptable_block_size:
            encrypt_data = msg[offset : offset + max_encryptable_block_size]
            ciphertext += cipher.encrypt(encrypt_data)
        else:
            ciphertext += cipher.encrypt(msg[offset:])

        offset += max_encryptable_block_size

    encrypted_msg = b64encode(ciphertext).decode('utf-8')
    print("Encrypted message:", encrypted_msg)
    return encrypted_msg

def decrypted(encrypted_msg):

    # 私鑰解密 - 分段解密
    max_decryptable_block_size = key.size_in_bytes() # 256

    ciphertext = b64decode(encrypted_msg.encode('utf-8'))
    length = len(ciphertext)

    offset = 0
    decrypted_message = ''.encode('utf-8')
    while length - offset > 0:
        if length - offset > max_decryptable_block_size:
            decrypted_data = ciphertext[offset : offset + max_decryptable_block_size]
            decrypted_message += decipher.decrypt(decrypted_data)
        else:
            decrypted_message += decipher.decrypt(ciphertext[offset:])

        offset += max_decryptable_block_size

    print("Decrypted message:", decrypted_message.decode('utf-8'))
    return decrypted_message.decode('utf-8')


random_numbers = [random.randint(0, 100) for _ in range(1000)]
random_numbers_str = ''.join(map(str, random_numbers))
plaintext = f"{random_numbers_str} Hello, World"
encrypted_msg = encrypted(plaintext)
decrypted(encrypted_msg)
