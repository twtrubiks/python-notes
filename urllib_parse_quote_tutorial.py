"""
https://docs.python.org/3/library/urllib.parse.html
"""

from urllib.parse import quote, unquote

# = becomes %3D
# + becomes %2B
# Original string with special characters
signature = "test/def+123=4666"

# URL encode the string
encoded_signature = quote(signature)

print("Original Signature:", signature)
print("URL Encoded Signature:", encoded_signature)

print("Restore Original Signature:", unquote(signature))
