from pathlib import Path


def get_files(target_dir: Path):

    if not target_dir.exists():
        print(f"The directory '{target_dir}' does not exist.")
        return []
    elif not target_dir.is_dir():
        print(f"'{target_dir}' is a file, not a directory.")
        return []
    else:
        files = [entry for entry in target_dir.iterdir() if entry.is_file()]
        return files