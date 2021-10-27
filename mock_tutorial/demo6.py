import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError
from my_user import get_users


class TestUsers(unittest.TestCase):

    # method_1
    def test_get_users(self):
        with patch('my_user.requests') as mock_requests:
            mock_requests.get.side_effect = HTTPError
            with self.assertRaises(HTTPError):
                get_users()

    # method_2
    # def test_get_users(self):
    #     with patch('my_user.requests', **{'get.side_effect': HTTPError}) as mock_requests:
    #         with self.assertRaises(HTTPError):
    #             get_users()

if __name__ == '__main__':
    unittest.main()

