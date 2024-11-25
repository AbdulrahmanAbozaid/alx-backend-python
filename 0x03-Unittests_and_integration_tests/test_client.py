#!/usr/bin/env python3
"""
Test the client Module
"""
import client
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import Any
from unittest import TestCase
from unittest.mock import PropertyMock, patch, Mock


class TestGithubOrgClient(TestCase):
    """Test Github Class"""

    @parameterized.expand(
        [
            ("google", 42),
            ("abc", 42),
        ]
    )
    @patch("client.get_json", new_callable=Mock)
    def test_org(self, org: str, expected: Any, mock_json: Mock) -> None:
        """Test the org func"""
        mock_json.return_value = 42
        git_org = client.GithubOrgClient(org)
        self.assertEqual(git_org.org, expected)
        mock_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Test public apis"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": 42}
            git_org = client.GithubOrgClient("google")
            self.assertEqual(git_org._public_repos_url, 42)

    @patch("client.get_json", new_callable=Mock)
    def test_public_repos(self, mock_json):
        """Test the PublicRepos method"""
        mock_json.return_value = [
            {"name": 1},
            {"name": 1},
            {"name": 1},
        ]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_repo:
            mock_repo.return_value = 42
            git_org = client.GithubOrgClient("google")
            self.assertSequenceEqual(git_org.public_repos(), [1, 1, 1])
            mock_json.assert_called_once()
            mock_repo.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, licence_key, expected):
        """Test the has licence func"""
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, licence_key), expected
        )


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

        def mocked_requests_get(url: str):
            """Mock for requests.get().json() behavior based on URL."""
            if "google/" not in url:
                return type("MockResponse", (object,),
                            {"json": lambda: cls.org_payload})
            elif "repos" in url:
                return type("MockResponse", (object,),
                            {"json": lambda: cls.repos_payload})
            return None

        cls.mock_get.side_effect = mocked_requests_get

    def test_public_repos(self):
        """Test the PublicRepos method"""
        git_org = client.GithubOrgClient("google")
        self.assertSequenceEqual(git_org.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the PublicRepos method"""
        git_org = client.GithubOrgClient("google")
        self.assertSequenceEqual(
            git_org.public_repos(license="apache-2.0"), self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
