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
