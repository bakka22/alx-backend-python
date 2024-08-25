#!/usr/bin/env python3
""" test cases for utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ test cases for utils.access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, mapped, path, expected):
        """ test normal range inputs for utils.access_nested_map """
        self.assertEqual(access_nested_map(mapped, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self,  nested_map, path):
        """ test invalid inputs """

        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ test cases for utils.get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    @patch('test_utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """ test functionality with normal values """
        mock_get.return_value.json.return_value = payload
        self.assertEqual(get_json(url), payload)
        mock_get.assert_called_once_with(url)
