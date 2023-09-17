"""
https://pypi.org/project/pycryptodome/

pip install pycryptodome
私鑰簽名, 公鑰驗簽

sign (簽名) 用 private key 私鑰
verify_sign (驗證簽名) 用 public key 公鑰
"""


from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode


def verify_sign(public_key_loc, signature, data):

    with open(public_key_loc, 'rb') as f:
        pub_key = RSA.import_key(f.read())

    digest = SHA256.new(data)
    verifier = PKCS1_v1_5.new(pub_key)
    if verifier.verify(digest, b64decode(signature)):
        return True
    return False


def sign(private_key_loc, message: str) -> str:
    with open(private_key_loc, 'rb') as f:
        priv_key = RSA.import_key(f.read())

    h = SHA256.new(message)
    signer = PKCS1_v1_5.new(priv_key)
    signature = signer.sign(h)
    return b64encode(signature).decode()


msg = "22222"
msg = msg.encode("utf-8")

# msg = b"22222"

signed_str = sign('private_key.pem', msg)
print("簽名:", signed_str)

result = verify_sign('public_key.pem', signed_str, msg)
print("驗證結果:", result)
