# Rename Special Characters Utility

This Python script recursively renames files and directories in a specified folder, replacing non-ASCII characters in their names with underscores (`_`). It is useful for cleaning up file and folder names that may cause compatibility issues due to special or non-English characters.

## Features
- Recursively traverses all subfolders and files in the target directory.
- Renames directories and files to remove non-ASCII characters.
- Handles name conflicts and prints all changes made.
- Two renaming strategies:
  - `Rename`: Replaces consecutive non-ASCII characters with a single underscore.
  - `Rename1`: Replaces every non-ASCII character with an underscore.

## Usage

### 1. Prerequisites
# Rename Special Characters Utility

A small command-line utility that renames files and directories by replacing non-ASCII characters in their basenames with underscores. The tool is intended to help make filenames more portable across systems that may not handle special characters consistently.

## Requirements
- Python 3.6 or later

## Key behaviors
- Recursive: walks the directory tree starting at the provided root path.
- Two renaming strategies:
  - `minimal` (default): collapse consecutive non-ASCII characters into a single underscore.
  - `all`: replace every non-ASCII character with an underscore.
- Safe collision handling: if the target name already exists, the tool appends a numeric suffix before the extension (e.g. `file.txt` -> `file_1.txt`).
- Dry-run mode shows the proposed final candidate name (including numeric suffix) without making changes.

## Usage
Run from a shell. If no path is provided the current directory (`.`) is used.

Examples (PowerShell):

```pwsh
# Show proposed renames without making changes
python rename_special_charecters.py --dry-run

# Rename contents under C:\data using default (minimal) mode
python rename_special_charecters.py C:\data

# Only process names containing the substring "project" and replace every non-ASCII char
python rename_special_charecters.py C:\data --pattern project --mode all
```

Options
- path (positional): Root path to process. Default: `.` (current directory)
- --mode {minimal,all}: Choose renaming strategy. Default: `minimal`
- --pattern PATTERN: Only rename files/directories whose name contains PATTERN (simple substring match)
- --dry-run: If set, print `DRY-RUN: <src> -> <candidate>` for each change and do not perform filesystem modifications

Notes
- The script applies renaming to basenames only and joins them with their existing parent paths (i.e. `os.path.join(root, new_name)`).
- Always run with `--dry-run` first to inspect changes.

License: MIT

