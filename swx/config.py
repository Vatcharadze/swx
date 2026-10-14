import argparse
from pathlib import Path

def get_dir_path():
    parser = argparse.ArgumentParser(description='Points to specified Directory')
    parser.add_argument('-p', '--path', required=True, help='Full path to directory to scan')
    args = parser.parse_args()
    return Path(args.path)


