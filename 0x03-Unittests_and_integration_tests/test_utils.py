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
        """ test normal range inputs for utils.access_nested_map """
        self.assertEqual(access_nested_map(mapped, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exeption(self, mapped, path, expected):
        """ test invalid inputs """
        with self.assertRaises(KeyError) as e:
            access_nested_map(mapped, path)
        self.assertEqual(e.exception.args[0], expected)
