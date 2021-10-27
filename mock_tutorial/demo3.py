import requests
import unittest
from unittest.mock import Mock

requests = Mock()

def get_users():
    r = requests.get('http://demo/api/users')
    print(r.status_code)
    if r.status_code == 200:
        return r.json()
    return None

class TestUsers(unittest.TestCase):

    def method_1(self):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            'id': 1,
            'user': 'twtrubiks',
        }
        return response_mock

    def method_2(self):
        data = {
            'status_code': 200,
            'json.return_value': {
                'id': 1,
                'user': 'twtrubiks'
            }
        }
        # unpacking a dictionary
        return Mock(**data)

    def mock_request(self, url):
        print('my requests {}'.format(url))

        response_mock = self.method_1()
        # response_mock = self.method_2()

        return response_mock

    def test_get_users(self):
        # Mock will invoke when you call your mocked method
        requests.get.side_effect = self.mock_request
        user = get_users()
        assert user['id'] == 1
        assert user['user'] == 'twtrubiks'

if __name__ == '__main__':
    unittest.main()
