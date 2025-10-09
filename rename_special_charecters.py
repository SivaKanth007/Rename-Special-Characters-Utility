import os
import argparse
import sys


def replace_non_ascii_minimal(s: str) -> str:
    """Replace runs of non-ASCII chars with a single underscore."""
    out = []
    prev_ascii = True
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
            prev_ascii = True
        else:
            if prev_ascii:
                out.append('_')
            prev_ascii = False
    return ''.join(out)


def replace_non_ascii_all(s: str) -> str:
    """Replace every non-ASCII char with an underscore."""
    return ''.join(ch if ord(ch) < 128 else '_' for ch in s)


def safe_rename(src: str, dst: str, dry_run: bool = False) -> bool:
    """Attempt to rename src -> dst. If target exists, append a counter before extension.

    Returns True if rename would be performed (or simulated in dry-run)."""
    if src == dst:
        return False
    base, ext = os.path.splitext(dst)
    candidate = dst
    i = 1
    while os.path.exists(candidate):
        candidate = f"{base}_{i}{ext}"
        i += 1
    if dry_run:
        print(f"DRY-RUN: {src} -> {candidate}")
        return True
    os.rename(src, candidate)
    print(f"RENAMED: {src} -> {candidate}")
    return True


def process_tree(path: str, mode: str = 'minimal', pattern: str = None, dry_run: bool = False):
    """Walk directory tree and rename files and directories to ASCII-only names.

    Args:
        path: root path to walk
        mode: 'minimal' (replace runs) or 'all' (replace every non-ASCII char)
        pattern: optional substring to filter filenames (simple contains)
        dry_run: if True, do not perform filesystem changes
    """
    replacer = replace_non_ascii_minimal if mode == 'minimal' else replace_non_ascii_all

    for root, dirs, files in os.walk(path, topdown=True):
        # Rename directories in-place (modify dirs list so walk continues correctly)
        for i, d in enumerate(list(dirs)):
            if pattern and pattern not in d:
                continue
            orig = os.path.join(root, d)
            new_name = replacer(d)
            if new_name != d:
                new = os.path.join(root, new_name)
                if safe_rename(orig, new, dry_run=dry_run):
                    # update the dirs list so os.walk will continue into the new dir name
                    dirs[i] = new_name

        for f in files:
            if pattern and pattern not in f:
                continue
            orig = os.path.join(root, f)
            new_name = replacer(f)
            if new_name != f:
                new = os.path.join(root, new_name)
                safe_rename(orig, new, dry_run=dry_run)


def build_parser():
    p = argparse.ArgumentParser(description='Rename files and directories by replacing non-ASCII characters with underscores')
    p.add_argument('path', nargs='?', default='.', help='Root path to process')
    p.add_argument('--mode', choices=['minimal', 'all'], default='minimal', help="'minimal' collapses runs of non-ASCII into one underscore; 'all' replaces every non-ASCII char")
    p.add_argument('--pattern', help='Only process names containing this substring')
    p.add_argument('--dry-run', action='store_true', help='Show what would be renamed without performing changes')
    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    if not os.path.exists(args.path):
        print(f"Path does not exist: {args.path}")
        return 2
    process_tree(args.path, mode=args.mode, pattern=args.pattern, dry_run=args.dry_run)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
