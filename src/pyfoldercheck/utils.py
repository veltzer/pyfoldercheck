""" utils.py """


def is_ascii(s, exceptions):
    return all(ord(c) < 128 or c in exceptions for c in s)


def add_non_ascii(set_to_add_to, string_to_scan):
    for c in string_to_scan:
        if ord(c) >= 128:
            set_to_add_to.add(c)


def has_character(c, s):
    return c in s
