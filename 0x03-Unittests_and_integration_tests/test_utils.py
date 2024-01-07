#!/usr/bin/env python3
"""
unitest using @parameterized decorator
"""

from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the functionality of access_nested_map
    function using @parameterized decorator
    """

    @parameterized.expand([({"a": {"b": 2}}, ("a", "b"), 2),
                           ({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2})])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        This function tests the 'access_nested_map' function by providing
        it with a nested map, a path, and an expected output. It then checks
        if the output of the 'access_nested_map' function matches the expected
        output.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",), KeyError),
                           ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Tests for keyError
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class tests if the get_json function works as expected.
    """
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        This test case tests the functionality of the get_json function.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
