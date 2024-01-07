#!/usr/bin/env python3
"""
unitest using @parameterized decorator
"""

from parameterized import parameterized, parameterized_class
from utils import access_nested_map
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
