#!/usr/bin/env python3
""" Module for testing utils """

import unittest
from parameterized import parameterized
from unittest import mock
from utils import (memoize, get_json, access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    """ Class for Testing Access Nested Map """


    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test that a KeyError is raised for the respective inputs """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"Key not found: {path[-1]}")


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """


    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch("your_module.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """


    @mock.patch("your_module.TestClass.a_method")
    def test_memoize(self, mock_a_method):
        """ Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """
        mock_a_method.return_value = 42

        class TestClass:
            """ Test Class for wrapping with memoize """

            
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_object = TestClass()

        # Call a_property twice
        result1 = test_object.a_property
        result2 = test_object.a_property

        mock_a_method.assert_called_once()
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)