"""Behavioural tests for pyfoldercheck's pure string helpers."""

import unittest

from pyfoldercheck import utils


class IsAsciiTests(unittest.TestCase):
    def test_plain_ascii_is_true(self) -> None:
        assert utils.is_ascii("hello world", set())

    def test_non_ascii_is_false(self) -> None:
        assert not utils.is_ascii("café", set())

    def test_non_ascii_in_exceptions_is_true(self) -> None:
        assert utils.is_ascii("café", {"é"})

    def test_empty_string_is_true(self) -> None:
        assert utils.is_ascii("", set())


class AddNonAsciiTests(unittest.TestCase):
    def test_collects_non_ascii_characters(self) -> None:
        found: set[str] = set()
        utils.add_non_ascii(found, "aébü")
        assert found == {"é", "ü"}

    def test_pure_ascii_adds_nothing(self) -> None:
        found: set[str] = set()
        utils.add_non_ascii(found, "plain")
        assert found == set()


class HasCharacterTests(unittest.TestCase):
    def test_present_character(self) -> None:
        assert utils.has_character("a", "banana")

    def test_absent_character(self) -> None:
        assert not utils.has_character("z", "banana")
