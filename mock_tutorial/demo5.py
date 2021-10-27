import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError
from my_user import get_users


class TestUsers(unittest.TestCase):

    # method_1
    @patch('my_user.requests')
    def test_get_users(self, mock_request):
        mock_request.get.side_effect = HTTPError
        with self.assertRaises(HTTPError):
            get_users()

    # method_2
    # @patch('my_user.requests', **{'get.side_effect': HTTPError})
    # def test_get_users(self, mock_request):
    #     with self.assertRaises(HTTPError):
    #         get_users()

if __name__ == '__main__':
    unittest.main()
