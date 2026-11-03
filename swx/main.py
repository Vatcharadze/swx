import subprocess

from swx import config, scan, sort


def run_sorter():
    try:
        dir_path = config.get_dir_path()
        files_to_sort = scan.get_files(dir_path)

        if not files_to_sort:
            print("No loose files found to organize.")
            return

        sort.organize_files(files_to_sort, dir_path)
        print("\nSorting complete!")
        subprocess.run(["ls", str(dir_path)], check=False)
    except (FileNotFoundError, PermissionError, NotADirectoryError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_sorter()
