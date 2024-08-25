#!/usr/bin/env python3
""" test cases for utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test cases for utils.access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, mapped, path, expected):
        """ test cases for utils.access_nested_map """
        self.assertEqual(access_nested_map(mapped, path), expected)
