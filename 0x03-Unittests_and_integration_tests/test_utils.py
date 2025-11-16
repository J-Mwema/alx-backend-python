#!/usr/bin/env python3
"""Test cases for utils.access_nested_map and get_json"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected payload"""
        # Mock requests.get
        with unittest.mock.patch('requests.get') as mock_get:
            # Configure mock to return an object with .json() method
            mock_response = unittest.mock.Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function
            result = get_json(test_url)

            # Assert: get was called once with correct URL
            mock_get.assert_called_once_with(test_url)
            # Assert: result matches payload
            self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test the memoize decorator"""

    def test_memoize(self):
        """Test that method is called once and result is cached"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create instance
        obj = TestClass()

        # Patch a_method
        with unittest.mock.patch.object(obj, 'a_method', return_value=42) as mock_method:
            # Call twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Assert: result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            # Assert: a_method called only once
            mock_method.assert_called_once()
