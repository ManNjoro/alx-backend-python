#!/usr/bin/env python3
"""
Test module for the GithubOrgClient class.
"""

from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient
from typing import Dict
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test module for the GithubOrgClient class.
    """
    response_dict = {"name": "company"}

    @parameterized.expand([('google', response_dict), ('abc', response_dict)])
    @patch('client.get_json',)
    def test_org(self, input: str, expected: Dict, mock_get_json):
        """
        Test the org method of the GithubOrgClient class.

        Parameters:
            input (str): The organization name.
            expected (Dict): The expected output.
            mock_get_json (Mock): A mock for the get_json function.
        """
        mock_get_json.return_value = expected
        org_client = GithubOrgClient(input)

        self.assertEqual(org_client.org(), expected)

        expected_url = f"https://api.github.com/orgs/{input}"
        mock_get_json.assert_called_once_with(expected_url)
