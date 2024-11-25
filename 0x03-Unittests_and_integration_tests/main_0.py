#!/usr/bin/env python3
"""
Main Module To Test
"""
from utils import access_nested_map, get_json
from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


with patch("__main__.get_json", new_callable=Mock) as mockJ:
    mockJ.json.return_value = 'foo'
    get_json.json('https://jsonplaceholder.typicode.com/posts/1')
    get_json.json.assert_called_once_with('shttps://jsonplaceholder.typicode.com/posts/1')

