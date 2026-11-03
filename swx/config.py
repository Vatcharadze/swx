import argparse
from pathlib import Path


def get_dir_path():
    parser = argparse.ArgumentParser(
        description='Sort files in a specified directory.',
        epilog=(
            'Examples:\n'
            '  swx -p ~/Downloads    Sort files in Downloads\n'
            '  swx -p .              Sort files in the current directory'
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-p',
        '--path',
        required=True,
        help='Path to the directory to sort. Use "." for the current directory.'
    )

    args = parser.parse_args()
    return Path(args.path)
