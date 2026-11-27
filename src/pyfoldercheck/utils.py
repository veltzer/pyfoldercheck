""" utils.py """

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Container



def is_ascii(s: str, exceptions: Container[str]) -> bool:
    return all(ord(c) < 128 or c in exceptions for c in s)


def add_non_ascii(set_to_add_to: set[str], string_to_scan: str) -> None:
    for c in string_to_scan:
        if ord(c) >= 128:
            set_to_add_to.add(c)


def has_character(c: str, s: str) -> bool:
    return c in s
