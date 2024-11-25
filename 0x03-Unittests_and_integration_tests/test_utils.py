#!/usr/bin/env python3
"""
Testing the utils Module functions
"""
from typing import Any, Mapping, Sequence
from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, memoize
import utils


class TestAccessNestedMap(TestCase):
    """Test the nested map func"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ) -> None:
        """test the inps"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, expected: str
    ):
        """test with exception"""
        with self.assertRaisesRegex(KeyError, expected):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Test get JSON func"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.get_json", new_callable=Mock)
    def test_get_json(self, url: str,
                      test_payload: dict, mock_api: Mock) -> None:
        """Test get json api"""
        mock_api.json.return_value = test_payload
        self.assertEqual(utils.get_json.json(url), test_payload)
        mock_api.json.assert_called_once_with(url)


class TestMemoize(TestCase):
    """Test Memoization decorator"""

    def test_memoize(self):
        """Test Memoize"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_m:
            mock_m.return_value = 42
            inst = TestClass()
            self.assertEqual(inst.a_property, 42)
            self.assertEqual(inst.a_property, 42)
            mock_m.assert_called_once()
