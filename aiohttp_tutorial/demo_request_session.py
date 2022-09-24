import requests

# Using a session as a best practice
# https://docs.aiohttp.org/en/stable/http_request_lifecycle.html#aiohttp-request-lifecycle

with requests.Session() as session:
    response = session.get('http://python.org')
    print(response.text)
