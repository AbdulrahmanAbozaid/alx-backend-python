#!/usr/bin/env python3
"""
Main Module To Test
"""
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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

        with patch("test_utils.TestClass.a_method", new_callable=Mock) as mock_m:
            mock_m.return_value = 42
            inst = TestClass()
            self.assertEqual(inst.a_property, 42)
            self.assertEqual(inst.a_property, 42)
            mock_m.assert_called_once()

print(__name__)