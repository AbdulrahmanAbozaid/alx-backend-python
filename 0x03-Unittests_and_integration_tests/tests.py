#!/usr/bin/env python3
"""
Main Module To Test
"""
import unittest
from parameterized import parameterized, parameterized_class


class TestStringMethods(unittest.TestCase):
    """test string methods functionality"""

    def test_upper(self):
        """ensure string in upper case"""
        self.assertEqual("foo".upper(), "FOO")

    @parameterized.expand(
        [
            (1, 2, 3),
            (4, 6, 10),
            (122, 232, 354),
        ]
    )
    def test_sum(self, a: int, b: int, expected: int) -> bool:
        self.assertEqual(sum((a, b)), expected, "Not Equal, Oh man")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    # unittest.main()
    pass