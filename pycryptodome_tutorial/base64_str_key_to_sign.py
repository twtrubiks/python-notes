"""
https://pypi.org/project/pycryptodome/

pip install pycryptodome
私鑰簽名, 公鑰驗簽

sign (簽名) 用 private key 私鑰 - str
verify_sign (驗證簽名) 用 public key 公鑰 - str
"""

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode

PRIVATE_KEY = "MIIEowIBAAKCAQEAsKEWO2gxoUfFOuXLfha0KsDHS2XhECf3GooIieKx/3/mYeBiZUbTlyA1+DANrE2CT2up6WDtkZGmfxsVIuLlvxEtdWzrcmHrVfhliAHuRxplfSCsJIMuEO8N2lnGTuqqs2+fIOMnDE74VMBWR+0yOsk037W9bXWZegOIvaoRopnx4siDPGarVBE8yMegxYDwVJ++5zbn1rQO71Y9mM3sA7/g5J5QZPXJEr2UbDDaMLhCR2y38GYjy5d8ShOF/psm346fR5uDeYrXr7l/YPs1Np/w0eH6mAQmJo4mIIcjhCyKjfEmqdfOITbs1caqxjZCw2pXnTC6Vc1UF2gZwfU/sQIDAQABAoIBADLEilRW9XTq4Ri1thCuy+hB8saMKO1w30iEhkHDo+/RPlHBoeaEPgsBGiIVBckRmjPjuTm4P3CI0bdU/HVDjE+ny04mGWKOHItgUyaNj4RmZOdbPb9c6R+65lttVF+YeaoLmkxknfOeuyf5BJO17KsS7Byk6yaMF6oHXAVP3bPDWmWEXSLbkpi7p7pAKEZes7kJfjUX8/cIuVQP5OPUPCez4l4LOqiNQczBHLEczqMVzrGvDQdHQLXt/UkPBAV/opPkSc4C+cXTWkxcaUFkyUGK2DNlukYJJrXHcOxp6PELf7isBKnM7efrJNFxI5sNrbVWaWOBTboDjETeelL3VYUCgYEAuR4RFNvTimrHLQWGM2AoWOfUIxiNOAIq0QcKt42EUeeTibXbsfnOOFlIBt67PwR+qc7vu7Xo2KyTxsuvKNQAwJmV5hhojKl6yojrJ37oYCQQrknL/kXY1ni26CHXguNs0CSkUpLaqV6PkavMOsHKHJCWe4ZcIVA2NMC/vGKUx7sCgYEA9EL5Mv+SQKroEcZ92yvDrn3AyZW+nXTS81cpVMT/NYQEFdB9b03XazAd+J0bzhVYtOwJRJsV1LFpum0kU1HwI7bvjddF4nwBUV1020bKX6zculqPNyEaPs0HRjSS4RLYzi7PpNbAzog6fO2HgQQenrQK0pBDhLax7qOODSSk8YMCgYAZ2GbOILryMmJImOLZvW0krIljtQPSdAsCUBdg9TMqNEjXCzr3KEdwepahzusZq0j78FZsQMOXrNCdCscTzjWkrkzNaU7/hJIOQPuD8iYDdkWV79u5TosttoDi/AaY0aPZk6QVm0dIKlmlHvVOpsvPHSjFakbmp8pJpzed162qDQKBgClljFxjSgMhs/EHRd82PJS/BURk14hR+0p4dC3EsUf9lr+ntQp/E8o7vmibH9I+dek7s5pn+jww0S1iP+zLDzrOTy0n1dU7lPGYOCzNg5DReBsxK+J4/ryz/M6eLGJu0kWnU1OpfcXC+r6fdv6blyDofIkRIBBG8kLyfymlEztHAoGBAK2df8qqVnD57HkpDSFBUofe0GcSih/Hq97hjtdKP2y2IGNhVnKYxXazjxS+PF78BacCLJrY3D7DW+g3pGDmtKjOY0jRoHm7BvUD9CLw79cNLfYxs8RCXlzBTTCufOT6fP3dRLhSaf+aksto3s4ZYH9BfUT6xkF0elgyldfPYqjR"
PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsKEWO2gxoUfFOuXLfha0KsDHS2XhECf3GooIieKx/3/mYeBiZUbTlyA1+DANrE2CT2up6WDtkZGmfxsVIuLlvxEtdWzrcmHrVfhliAHuRxplfSCsJIMuEO8N2lnGTuqqs2+fIOMnDE74VMBWR+0yOsk037W9bXWZegOIvaoRopnx4siDPGarVBE8yMegxYDwVJ++5zbn1rQO71Y9mM3sA7/g5J5QZPXJEr2UbDDaMLhCR2y38GYjy5d8ShOF/psm346fR5uDeYrXr7l/YPs1Np/w0eH6mAQmJo4mIIcjhCyKjfEmqdfOITbs1caqxjZCw2pXnTC6Vc1UF2gZwfU/sQIDAQAB"


# def der_to_b64encode_str(key_loc):
#     with open(key_loc, 'rb') as f:
#         return b64encode(f.read())

# def der_to_str():
#     PRIVATE_KEY = der_to_b64encode_str("private_key.der")
#     PUBLIC_KEY = der_to_b64encode_str("public_key.der")
#     print("PRIVATE_KEY:", PRIVATE_KEY)
#     print("PUBLIC_KEY:", PUBLIC_KEY)


def str_to_b64decode_der(data):
    return b64decode(data)

def verify_sign(key_str:str, signature, data):

    pub_key = RSA.import_key(str_to_b64decode_der(key_str))

    digest = SHA256.new(data)
    verifier = PKCS1_v1_5.new(pub_key)
    if verifier.verify(digest, b64decode(signature)):
        return True
    return False

def sign(key_str:str, message: str) -> str:

    priv_key = RSA.import_key(str_to_b64decode_der(key_str))

    h = SHA256.new(message)
    signer = PKCS1_v1_5.new(priv_key)
    signature = signer.sign(h)
    return b64encode(signature).decode()


msg = "22222"
msg = msg.encode("utf-8")

signed_str = sign(PRIVATE_KEY, msg)
print("簽名:", signed_str)

result = verify_sign(PUBLIC_KEY, signed_str, msg)
print("驗證結果:", result)