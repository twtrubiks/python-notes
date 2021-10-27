import requests
import unittest
from unittest.mock import Mock
from requests.exceptions import HTTPError

requests = Mock()

def get_users():
    r = requests.get('http://demo/api/users')
    if r.status_code == 200:
        return r.json()
    return None

class TestUsers(unittest.TestCase):

    def test_get_users_retry(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            'id': 1,
            'user': 'twtrubiks',
        }
        requests.get.side_effect = [response_mock, HTTPError]
        user = get_users()
        assert user['id'] == 1
        assert user['user'] == 'twtrubiks'

        with self.assertRaises(HTTPError):
            get_users()

if __name__ == '__main__':
    unittest.main()
