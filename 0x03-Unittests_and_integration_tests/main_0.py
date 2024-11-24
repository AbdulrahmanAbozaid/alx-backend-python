#!/usr/bin/env python3
"""
Main Module To Test
"""
from utils import access_nested_map


m = {"user": {"address": {"city": "alex"}}}

print(access_nested_map(m, ['user', 'address']) == {'city': 'alex'})
