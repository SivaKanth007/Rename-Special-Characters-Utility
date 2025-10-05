import os

def rename_ascii(name):
    """
    Replace non-ASCII characters in 'name' with underscores, but only insert one underscore for consecutive non-ASCII characters.
    Args:
        name (str): The original file or directory name.
    Returns:
        str: The ASCII-only name with underscores replacing non-ASCII sequences.
    """
    res, prev = [], True
    for c in name:
        if ord(c) < 128:  # ASCII character
            res.append(c)
            prev = True
        elif prev:        # First non-ASCII in a sequence
            res.append('_')
            prev = False
    return ''.join(res)

def rename_all_ascii(name):
    """
    Replace every non-ASCII character in 'name' with an underscore.
    Args:
        name (str): The original file or directory name.
    Returns:
        str: The ASCII-only name with underscores replacing all non-ASCII characters.
    """
    return ''.join(c if ord(c) < 128 else '_' for c in name)

def rename_dirs(root, dirs):
    """
    Rename all directories in 'dirs' under 'root' to ASCII-only names.
    Args:
        root (str): The parent directory path.
        dirs (list): List of directory names to process.
    """
    for d in dirs:
        orig = os.path.join(root, d)
        new = rename_ascii(orig)
        if new != orig:
            try:
                os.rename(orig, new)  # Try renaming using minimal underscores
                print(f"{orig}\n{new}")
            except OSError:
                # If failed, try renaming with all non-ASCII replaced
                new = rename_all_ascii(orig)
                print(f"{orig}\n{new}")
                os.rename(orig, new)

def list_pattern_files(path, pattern):
    """
    Walk through the directory tree starting at 'path', renaming directories and files to ASCII-only names.
    Args:
        path (str): Root directory to start walking.
        pattern (str): File pattern (unused in current code).
    """
    for root, dirs, files in os.walk(path):
        rename_dirs(root, dirs)  # Rename directories first
        for f in files:
            orig = os.path.join(root, f)
            new = rename_ascii(orig)
            if new != orig:
                try:
                    os.rename(orig, new)  # Try renaming using minimal underscores
                    print(f"{orig}\n{new}")
                except OSError as e:
                    # Handle case where target file already exists
                    if "file already exists" in str(e):
                        print(f"Failed: {e}")
                        new = rename_all_ascii(orig)
                        parts = new.rsplit('.', 1)
                        if len(parts) == 2:
                            # Add extra underscore before extension if needed
                            new = f"{parts[0]}_.{parts[1]}"
                        print(f"{orig}\n{new}")
                        os.rename(orig, new)
                    else:
                        print(f"Failed: {e}")

# Set the root path to process
path = "E:\\Mega"
list_pattern_files(path, ".mega")
