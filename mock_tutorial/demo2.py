from requests.exceptions import HTTPError
from unittest.mock import Mock

requests = Mock()

def get_users():
    r = requests.get('http://demo/api/users')
    if r.status_code == 200:
        return r.json()
    return None

if __name__ == '__main__':
    requests.get.side_effect = HTTPError
    try:
        get_users()
    except HTTPError:
        print('HTTPError')

    # Assert that the mock was called exactly once.
    requests.get.assert_called_once()


    # try:
    #     get_users()
    # except HTTPError:
    #     print('HTTPError')

    # # AssertionError: Expected 'get' to have been called once. Called 2 times
    # requests.get.assert_called_once()