#!/usr/bin/env python3
""" doc doc doc """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """doc doc doc"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """doc doc doc"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """doc doc doc"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """doc doc doc"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """doc doc doc"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

class TestMemoize(TestCase):
    """Test cases for the memoize decorator."""
    def test_memoize(self):
        """Test the memoize decorator on a property by mocking a_method."""
        class TestClass:
            """Dummy class for testing."""
            def a_method(self) -> int:
                """Mocked method for testing purposes."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Property under test using the memoize decorator."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked_method:
            mocked_method.return_value = 42
            dummy = TestClass()
            res1 = dummy.a_property
            res2 = dummy.a_property

        dummy = TestClass()
        res1 = dummy.a_property
        res2 = dummy.a_property

        mocked_method.assert_called_once()
        self.assertEqual(res1, 42)
        self.assertEqual(res2, 42)
