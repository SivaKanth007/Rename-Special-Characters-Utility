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
- Python 3.x installed on your system.

### 2. Setup
- Place the script (`rename_special_charecters.py`) in your desired directory.
- Edit the `path` variable in the script to point to the folder you want to process. Example:
  ```python
  path = "C:\\path\\to\\your\\target\\folder"
  ```

### 3. Run the Script
Open a terminal (PowerShell, Command Prompt, etc.), navigate to the script's directory, and run:
```pwsh
python rename_special_charecters.py
```

### 4. What Happens
- The script will walk through all files and folders under the specified path.
- It will rename any file or folder containing non-ASCII characters in its name, replacing those characters with underscores.
- All changes will be printed to the terminal for review.

## Code Documentation

### Functions

#### `Rename(name)`
- Input: `name` (str) — The file or directory name.
- Output: Renamed string with consecutive non-ASCII characters replaced by a single underscore.
- Logic: Iterates through each character, checks if it is ASCII, and builds the new name accordingly.

#### `Rename1(name)`
- Input: `name` (str) — The file or directory name.
- Output: Renamed string with every non-ASCII character replaced by an underscore.
- Logic: Iterates through each character, replaces non-ASCII with `_`.

#### `rename_dirs(root, dirs)`
- Input: `root` (str), `dirs` (list of str) — The current directory and its subdirectories.
- Output: None
- Logic: Renames each directory using `Rename`. If a conflict/error occurs, uses `Rename1`.

#### `list_pattern_files(path, pattern)`
- Input: `path` (str), `pattern` (str) — The root directory and file pattern (not actively used).
- Output: None
- Logic: Walks through the directory tree, renames directories and files using the above functions, handles conflicts, and prints changes.

### Main Execution
- Set the `path` variable to your target directory.
- Call `list_pattern_files(path, pattern)` to start the renaming process.

## Notes
- The script does not delete any files or directories.
- Commented code is present for pattern-based deletion, but is not active by default.
- Always back up your data before running bulk renaming scripts.

## Example Output
```
C:\path\to\your\target\folder\földér
C:\path\to\your\target\folder\f_ld_r
```

## License
MIT License
