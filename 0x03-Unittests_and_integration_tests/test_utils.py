#!/usr/bin/env python3
""" test cases for utils module """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """ test cases for utils.memoize """

    def test_memoize(self):
        """ test functionality of memoize decorator """
        class TestClass:
            """ test class """
            def a_method(self):
                """ tester method """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_a:
            tmp = TestClass()
            x = tmp.a_property
            c = tmp.a_property
            self.assertEqual(x, c)
            mock_a.assert_called_once_with()
