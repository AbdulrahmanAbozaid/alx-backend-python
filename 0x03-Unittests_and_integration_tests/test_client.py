#!/usr/bin/env python3
"""
Test the client Module
"""
from typing import Any
import client
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, Mock


class TestGithubOrgClient(TestCase):
    """Test Github Class"""

    @parameterized.expand([
        ('google', 42),
        ('abc', 42),
    ])
    @patch("client.get_json", new_callable=Mock)
    def test_org(self, org: str, expected: Any, mock_json: Mock) -> None:
        """Test the org func"""
        mock_json.return_value = 42
        git_org = client.GithubOrgClient(org)
        self.assertEqual(git_org.org, expected)
        mock_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")
