"""
可以使用以下的網站確認
https://www.freeformatter.com/hmac-generator.html
"""

import hashlib
import hmac

wait_to_sign_str = "hello world twtrubiks"
my_key = "aaa-bbb-ccc-ddd-token"

# HMAC-SHA256 簽章
hmac_sha256 = hmac.new(
    my_key.encode("utf-8"), wait_to_sign_str.encode("utf-8"), hashlib.sha256
)

print(hmac_sha256.hexdigest())