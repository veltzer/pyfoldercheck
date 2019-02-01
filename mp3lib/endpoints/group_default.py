import os

from pytconf.config import register_endpoint, register_function_group

from mp3lib.configs import ConfigRepository, ConfigNames

GROUP_NAME_DEFAULT = "default"
GROUP_DESCRIPTION_DEFAULT = "all pytsv commands"


def register_group_default():
    register_function_group(
            function_group_name=GROUP_NAME_DEFAULT,
            function_group_description=GROUP_DESCRIPTION_DEFAULT,
    )


def is_ascii(s, exceptions):
    for c in s:
        if ord(c) >= 128 and c not in exceptions:
            return False
    return True
    # return all(ord(c) < 128 for c in s)


def add_non_ascii(set_to_add_to, string_to_scan):
    for c in string_to_scan:
        if ord(c) >= 128:
            set_to_add_to.add(c)


def has_character(c, s):
    return c in s


@register_endpoint(
    configs=[
        ConfigRepository,
    ],
    suggest_configs=[
    ],
    group=GROUP_NAME_DEFAULT,
)
def scan():
    # type: () -> None
    """
    Scan the folder
    """
    bad_characters = set()
    chars_ok_for_folders = ""
    chars_ok_for_files = "“”ìú"
    count = 0
    for root, directories, files in os.walk(ConfigRepository.folder):
        for file in files:
            if 'á' in file:
                full = os.path.join(root, file)
                print(file, full)
                count += 1
            if not is_ascii(file, chars_ok_for_files):
                # full = os.path.join(root, file)
                # print(file, full)
                add_non_ascii(bad_characters, file)
        for directory in directories:
            if not is_ascii(directory, chars_ok_for_folders):
                full = os.path.join(root, directory)
                print('folder [{}]'.format(full))
    print(bad_characters)
    print("found [{}] appearances".format(count))


@register_endpoint(
    configs=[
        ConfigRepository,
        ConfigNames,
    ],
    suggest_configs=[
    ],
    group=GROUP_NAME_DEFAULT,
)
def scan():
    # type: () -> None
    """
    Authorize names with non ascii in them
    Only checks for name not previously authorized
    """
    bad_characters = set()
    chars_ok_for_folders = ""
    chars_ok_for_files = "“”ìú"
    count = 0
    for root, directories, files in os.walk(ConfigRepository.folder):
        for file in files:
            if 'á' in file:
                full = os.path.join(root, file)
                print(file, full)
                count += 1
            if not is_ascii(file, chars_ok_for_files):
                # full = os.path.join(root, file)
                # print(file, full)
                add_non_ascii(bad_characters, file)
        for directory in directories:
            if not is_ascii(directory, chars_ok_for_folders):
                full = os.path.join(root, directory)
                print('folder [{}]'.format(full))
    print(bad_characters)
    print("found [{}] appearances".format(count))

