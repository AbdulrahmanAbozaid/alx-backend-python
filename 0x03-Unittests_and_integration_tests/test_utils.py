#!/usr/bin/env python3
"""
Testing the utils Module functions
"""
from typing import Any, Mapping, Sequence
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


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
