import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError
from my_user import get_users, requests

class TestUsers(unittest.TestCase):

    @patch.object(requests, 'get', side_effect=HTTPError)
    def test_get_users(self, mock_requests):
        with self.assertRaises(HTTPError):
            get_users()

if __name__ == '__main__':
    unittest.main()

