# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pyfoldercheck/main.py:53-63` - the `review_not_ascii` endpoint ("Authorize words with non ascii in them") does nothing: it loads the JSON repository, calls `scan_files()` and throws away its result, then writes the same JSON back unchanged. `ConfigNames.repository_backup` and `ConfigNames.all_over` (`src/pyfoldercheck/configs.py:25-32`) are never read. Implement the review/authorize loop (compare found names against the repository, prompt, save, write the backup) or remove the endpoint and its unused config params.
- `src/pyfoldercheck/configs.py:12,23,27` - defaults are the author's private paths (`/mnt/seagate/mark/...`, `/home/mark/.mp3lib_authorized_non_ascii.json[.back]`) on a package published to PyPI; with `create_existing_folder`/`create_existing_file` every endpoint fails for any other user (and for the author on a machine without that disk) unless all paths are passed. Make these required parameters or default to something portable (e.g. the current directory, an XDG config path).

## Medium

- `src/pyfoldercheck/main.py:19-22` - leftover debug code: every file whose name contains the literal `"á"` is printed and counted, and `scan` (`main.py:43`) reports that count as "found [N] appearances". Remove the hardcoded character check and the count, or turn it into a real configurable search.
- `src/pyfoldercheck/main.py:23,28` - `Authorized.chars_ok_for_files`/`chars_ok_for_folders` are used, but `Authorized` is not listed in either endpoint's `configs=[...]` (`main.py:36-38,48-51`), so these can never be set from the command line and only the hardcoded defaults (`configs.py:41,45`) apply. Add `Authorized` to the endpoints' configs.
- `src/pyfoldercheck/main.py:14` - `scan_files` and both endpoints have no tests; only `utils.py` is covered (`tests/unit_tests/test_utils.py`). Add a test that runs `scan_files` against a `tmp_path` tree with non-ASCII file and folder names.

## Low

- `src/pyfoldercheck/utils.py:9` - dead commented-out alternative implementation after `return True`; delete it.
- `src/pyfoldercheck/utils.py:18` - `has_character` is never used by the package (only by its own test); remove it with its test.
- `src/pyfoldercheck/main.py:24-25` - commented-out debug prints; delete.
- `config/project.lua:4-7` - keywords `mp3`, `pdf`, `collection` do not describe a folder/filename checker; replace with e.g. `filenames`, `unicode`, `ascii`, `lint`, and the same list in `pyproject.toml:18-22`.
- `doc/TODO.txt` - empty file; delete it.
