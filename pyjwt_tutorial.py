import jwt
import time
from Crypto.PublicKey import RSA
from datetime import datetime, timedelta, timezone

"""
https://pyjwt.readthedocs.io/en/stable/

pip3 install pyjwt

"""

def load_key(my_key):
    with open(my_key, 'rb') as f:
        key = RSA.import_key(f.read())
    return key.export_key()

def ex1():
    """
    base
    """
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    print(encoded_jwt)

    decode_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    print(decode_jwt)

def ex2():
    """
    Encoding & Decoding Tokens with RS256 (RSA)
    https://pyjwt.readthedocs.io/en/stable/usage.html#encoding-decoding-tokens-with-rs256-rsa
    RSA 私鑰簽名, 公鑰驗證
    """
    private_key = load_key("private_key.pem")
    public_key = load_key("public_key.pem")
    print("private_key:", private_key)
    print("public_key:", public_key)

    # 私鑰簽名
    encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
    print("私鑰簽名:", encoded)

    # 公鑰驗證
    decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
    print("公鑰 decoded:", decoded)

def ex3():
    """
    Expiration Time Claim (exp)
    """
    # token_exp = jwt.encode({"username":"joe", "exp": datetime.utcnow() + timedelta(minutes=1)}, "mykey123", algorithm='HS256')

    jwt_payload = jwt.encode(
        {"exp": datetime.now(tz=timezone.utc) + timedelta(seconds=30)},
        "secret", algorithm="HS256"
    )
    decode_1 = jwt.decode(jwt_payload, "secret", algorithms=["HS256"])
    print("decode_1:", decode_1)

    time.sleep(32)

    """
    JWT payload is now expired
    But with some leeway(sec), it will still validate
    """
    decode_leeway = jwt.decode(jwt_payload, "secret", leeway=10, algorithms=["HS256"])
    print("decode_leeway:", decode_leeway)

    # Signature has expired
    jwt.decode(jwt_payload, "secret", algorithms=["HS256"])


if __name__ == '__main__':
    ex1()
    # ex2()
    # ex3()
