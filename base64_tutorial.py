from base64 import b64encode, b64decode


# encoded_data = b64encode(b'hello').decode()
# or
encoded_data = b64encode('hello'.encode("utf-8")).decode()
print("encoded_data:", encoded_data)

decoded_data = b64decode("aGVsbG8=")
print("decoded_data:", decoded_data.decode())

