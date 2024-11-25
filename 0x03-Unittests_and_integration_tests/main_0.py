#!/usr/bin/env python3
"""
Main Module To Test
"""
import client
from fixtures import TEST_PAYLOAD
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json
import utils


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        }
    ]
)
class TestIntegrationGithubOrgClient(TestCase):
    """Test Integration of public_repos"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = cls.mocked_requests_get

    @classmethod
    def mocked_requests_get(cls, url):
        """Mock for requests.get().json() behavior based on URL."""
        if "google/" not in url:
            return type("MockResponse", (object,), {"json": lambda: cls.org_payload})
        elif "repos" in url:
            return type("MockResponse", (object,), {"json": lambda: cls.repos_payload})
        return None

    def test_public_repos(self):
        """Test the PublicRepos method"""
        git_org = client.GithubOrgClient("google")
        self.assertSequenceEqual(git_org.public_repos(), self.expected_repos)

    def test_public_repos_license(self):
        """Test the PublicRepos method"""
        git_org = client.GithubOrgClient("google")
        self.assertSequenceEqual(
            git_org.public_repos(license="apache-2.0"), self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
