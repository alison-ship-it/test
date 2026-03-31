"""Tests for src.utils."""

import pytest
from src.utils import is_valid_email, clamp, word_frequencies, flatten, chunk


class TestIsValidEmail:
    def test_valid(self):
        assert is_valid_email("alice@example.com") is True

    def test_missing_at(self):
        assert is_valid_email("alice.example.com") is False

    def test_missing_domain(self):
        assert is_valid_email("alice@") is False


class TestClamp:
    def test_within_range(self):
        assert clamp(5, 0, 10) == 5

    def test_below_range(self):
        assert clamp(-3, 0, 10) == 0

    def test_above_range(self):
        assert clamp(15, 0, 10) == 10


class TestWordFrequencies:
    def test_simple(self):
        assert word_frequencies("hello world hello") == {"hello": 2, "world": 1}

    def test_empty(self):
        assert word_frequencies("") == {}


class TestFlatten:
    def test_nested(self):
        assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

    def test_flat(self):
        assert flatten([1, 2, 3]) == [1, 2, 3]


class TestChunk:
    def test_even_split(self):
        assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_remainder(self):
        assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
