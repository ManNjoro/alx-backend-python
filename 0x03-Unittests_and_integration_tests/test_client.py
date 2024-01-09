#!/usr/bin/env python3
"""
Test module for the GithubOrgClient class.
"""

from parameterized import parameterized, parameterized_class
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError
from typing import Dict
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test module for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", {'name': "google"}),
        ("abc", {'name': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, input: str, expected: Dict, mocked_fxn: MagicMock):
        """
        Test the org method of the GithubOrgClient class.

        Parameters:
            input (str): The organization name.
            expected (Dict): The expected output.
            mock_get_json (Mock): A mock for the get_json function.
        """
        mocked_fxn.return_value = MagicMock(return_value=expected)
        gh_org_client = GithubOrgClient(input)
        self.assertEqual(gh_org_client.org(), expected)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(input)
        )

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        This test case verifies the correct functioning
        of the '_public_repos_url' method.
        """
        mock_payload = {
            "public_repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        mock_org.return_value = mock_payload

        org_client = GithubOrgClient("testorg")

        public_repos_url = org_client._public_repos_url

        expected_url = "https://api.github.com/orgs/testorg/repos"
        self.assertEqual(public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock):
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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
