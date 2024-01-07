#!/usr/bin/env python3
"""
Test module for the GithubOrgClient class.
"""

from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from typing import Dict
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test module for the GithubOrgClient class.
    """
    response_dict1 = {"name": "google"}
    response_dict2 = {"name": "abc"}

    @parameterized.expand([
        ('google', response_dict1), ('abc', response_dict2)])
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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        mock_payload = {
            "public_repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        mock_org.return_value = mock_payload

        org_client = GithubOrgClient("testorg")

        public_repos_url = org_client._public_repos_url

        expected_url = "https://api.github.com/orgs/testorg/repos"
        self.assertEqual(public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Tests the `public_repos` method."""

        example_payload = [
            {"name": "repoA"},
            {"name": "repoB"},

        ]

        mock_get_json.return_value = example_payload

        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = """
            https://api.github.com/users/example/repos"""

            self.assertEqual(
                GithubOrgClient("example").public_repos(),
                ["repoA", "repoB"],
            )

            mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, expected):
        """
        Test if has license or not
        """
        github_client = GithubOrgClient('dummy')
        self.assertEqual(
            github_client.has_license(repo, license_key), expected)
