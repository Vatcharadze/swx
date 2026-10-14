# swx — Folder Sorter

**swx** (`swx-foldersorter`) is a small Python command-line tool that tidies up a messy folder. Point it at a directory and it moves every loose file into a sub-folder (`Documents`, `Images`, `Videos`, …) based on the file's extension.

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)

---

## Table of Contents

- [What it does](#what-it-does)
- [Requirements](#requirements)
- [Installation](#installation)
- [Verify the installation](#verify-the-installation)
- [Usage](#usage)
- [Example](#example)
- [Sorting rules](#sorting-rules)
- [Customizing the rules](#customizing-the-rules)
- [Project structure](#project-structure)
- [How it works](#how-it-works)
- [Important notes and limitations](#important-notes-and-limitations)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Author](#author)

---

## What it does

1. You give `swx` a directory with the `-p` / `--path` option.
2. It scans that directory and collects every **file** directly inside it (sub-folders are left alone).
3. For each file it looks at the extension (case-insensitive, so `.JPG` and `.jpg` are treated the same) and decides which category folder it belongs to.
4. It creates the category folder if it doesn't exist yet and moves the file into it.
5. Files with an extension that isn't in the rules go into an `Others` folder.
6. When finished it prints `Sorting complete!` and lists the directory contents.

If the directory has no loose files, it prints `No loose files found to organize.` and exits without changing anything.

## Requirements

- **Python 3.7 or newer**
- **pip** (included with Python)
- **Git** (only needed to clone the repository)
- No third-party Python packages. swx uses only the standard library.

Check your versions:

```bash
python --version
pip --version
git --version
```

On some systems the commands are `python3` and `pip3`.

## Installation

There are two ways to install swx. **Option 1 (pipx)** is the easiest: one command, no manual download, and the `swx` command works from any directory.

### Option 1: Install with pipx (recommended)

[pipx](https://pipx.pypa.io) installs Python command-line tools in their own isolated environments and puts the command on your `PATH`.

**Step 1. Install pipx** (skip if you already have it):

- **macOS (Homebrew):** `brew install pipx`
- **Debian / Ubuntu:** `sudo apt install pipx`
- **Windows or any OS with pip:**
  ```bash
  python -m pip install --user pipx
  ```

**Step 2. Add pipx's folder to your `PATH`:**

```bash
pipx ensurepath
```

Close and reopen your terminal afterwards.

**Step 3. Install swx straight from GitHub:**

```bash
pipx install git+https://github.com/Vatcharadze/swx.git
```

pipx clones the repository behind the scenes, builds it in its own virtual environment, and exposes the `swx` command globally.

**Step 4. Use it from anywhere:**

```bash
swx -p /path/to/your/folder
```

**Update to the latest version later:**

```bash
pipx upgrade swx-foldersorter
```

**Uninstall:**

```bash
pipx uninstall swx-foldersorter
```

### Option 2: Install from source with pip

Use this if you want a local copy of the code (for example, to edit the sorting rules).

#### Step 1: Clone the repository

```bash
git clone https://github.com/Vatcharadze/swx.git
```

#### Step 2: Enter the project folder

```bash
cd swx
```

#### Step 3 (recommended): Create and activate a virtual environment

A virtual environment keeps swx isolated from the rest of your system.

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
- **Windows (Command Prompt):** `.venv\Scripts\activate.bat`
- **macOS / Linux:** `source .venv/bin/activate`

You can skip this step and install globally, but a virtual environment is cleaner.

#### Step 4: Install the package

```bash
pip install .
```

This reads `pyproject.toml`, builds the `swx-foldersorter` package, and registers the `swx` command.

**Developing or modifying the code?** Use an editable install instead, so your changes apply immediately:

```bash
pip install -e .
```

## Verify the installation

Show the built-in help:

```bash
swx --help
```

You should see the `-p` / `--path` option described. You can also confirm pip registered the package:

```bash
pip show swx-foldersorter
```

## Usage

```bash
swx -p /full/path/to/folder
```

| Option          | Required | Description                         |
| --------------- | -------- | ----------------------------------- |
| `-p`, `--path`  | Yes      | Full path to the directory to scan  |
| `-h`, `--help`  | No       | Show help and exit                  |

Examples:

```bash
# macOS / Linux
swx -p ~/Downloads

# Windows
swx -p "C:\Users\YourName\Downloads"
```

> **Tip:** Try it on a test folder with a few dummy files first. Moving files is not automatically undoable.

You can also run it without the installed command, from the repository folder:

```bash
python -m swx.main -p /full/path/to/folder
```

## Example

Before:

```
Downloads/
├── holiday.jpg
├── report.pdf
├── budget.xlsx
├── backup.zip
├── movie.mp4
├── song.mp3
├── script.py
├── setup.exe
└── mystery.xyz
```

Run:

```bash
swx -p ~/Downloads
```

After:

```
Downloads/
├── Documents/
│   └── report.pdf
├── Spreadsheets/
│   └── budget.xlsx
├── Images/
│   └── holiday.jpg
├── Videos/
│   └── movie.mp4
├── Audio/
│   └── song.mp3
├── Archives/
│   └── backup.zip
├── Code/
│   └── script.py
├── Installers/
│   └── setup.exe
└── Others/
    └── mystery.xyz
```

## Sorting rules

| Folder            | Extensions                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------- |
| **Documents**     | `.pdf` `.docx` `.doc` `.txt` `.rtf` `.odt` `.md` `.pages`                                |
| **Spreadsheets**  | `.xlsx` `.xls` `.csv` `.ods`                                                             |
| **Presentations** | `.pptx` `.ppt` `.key`                                                                    |
| **Images**        | `.png` `.jpg` `.jpeg` `.gif` `.bmp` `.tiff` `.tif` `.svg` `.webp` `.heic` `.psd` `.ai`   |
| **Videos**        | `.mp4` `.mkv` `.mov` `.avi` `.flv` `.wmv` `.webm` `.m4v`                                 |
| **Audio**         | `.mp3` `.wav` `.aac` `.flac` `.ogg` `.m4a` `.wma`                                        |
| **Archives**      | `.zip` `.rar` `.7z` `.tar` `.gz` `.pkg` `.dmg`                                           |
| **Code**          | `.py` `.js` `.html` `.css` `.json` `.xml` `.sh` `.c` `.cpp` `.java`                      |
| **Installers**    | `.exe` `.msi` `.apk`                                                                     |
| **Others**        | Anything not listed above, including files with no extension                             |

## Customizing the rules

All rules live in one dictionary, `EXTENSION_MAP`, in `swx/extension_dict.py`. To add or change a rule, edit that file:

```python
EXTENSION_MAP = {
    '.pdf': 'Documents',
    '.epub': 'Books',      # new rule: .epub files go into a "Books" folder
    # ...
}
```

Extensions must be lowercase and include the leading dot. If you installed with `pip install .` (not editable), reinstall after editing, or use `pip install -e .` from the start.

## Project structure

```
swx/
├── swx/
│   ├── __init__.py
│   ├── main.py             # Entry point: run_sorter()
│   ├── config.py           # Parses the -p / --path argument
│   ├── scan.py             # Validates the path and lists files
│   ├── sort.py             # Creates folders and moves files
│   └── extension_dict.py   # EXTENSION_MAP: extension -> folder name
├── .gitignore
├── pyproject.toml          # Package metadata; defines the `swx` command
└── README.md
```

## How it works

1. `pyproject.toml` declares the console script `swx = swx.main:run_sorter`, so pip creates a `swx` command on install.
2. `main.run_sorter()` calls `config.get_dir_path()`, which uses `argparse` to read `-p/--path` and returns a `Path`.
3. `scan.get_files()` checks that the path exists and is a directory, then returns only the files directly inside it (not sub-folders, not recursive).
4. `sort.organize_files()` looks up each file's lowercase suffix in `EXTENSION_MAP` (defaulting to `Others`), creates the target folder with `mkdir(exist_ok=True)`, and moves the file with `Path.rename()`.
5. `run_sorter()` prints a completion message and lists the directory with `ls`.

## Important notes and limitations

- **Not recursive.** Only files directly inside the given folder are sorted. Files already inside sub-folders are untouched.
- **Hidden files are included.** Dotfiles (such as `.gitignore`) have no extension and will be moved to `Others`.
- **Name collisions.** If a file with the same name already exists in the destination folder, the behavior depends on your OS: on Windows, Python raises an error and sorting stops; on macOS/Linux, the existing file is silently overwritten. Avoid running swx on folders where this could happen, or back up first.
- **No undo or dry-run mode.** Files are moved immediately.
- **Final listing uses `ls`.** After sorting, swx runs the `ls` command to display the folder. On Windows (without Unix tools installed), this step fails with an error message, but **the sorting itself has already finished**.
- **Errors are printed, not raised.** Any exception is caught in `run_sorter()` and printed as a message.

## Uninstall

If you installed with pipx:

```bash
pipx uninstall swx-foldersorter
```

If you installed with pip:

```bash
pip uninstall swx-foldersorter
```

## Troubleshooting

**`swx: command not found` / `'swx' is not recognized`**
If you used pipx, run `pipx ensurepath` and reopen your terminal. Otherwise, the folder where pip puts scripts isn't on your `PATH`.
- Windows: add your Python `Scripts` folder (for example `%APPDATA%\Python\Python3x\Scripts`, or `.venv\Scripts` for a virtual environment) to `PATH`, then reopen the terminal.
- macOS / Linux: add `~/.local/bin` to `PATH`: `export PATH="$HOME/.local/bin:$PATH"`.
- Or skip the command and use `python -m swx.main -p <folder>` from the repository folder.

**`error: the following arguments are required: -p/--path`**
You ran `swx` without a path. Use `swx -p <folder>`.

**`The directory '...' does not exist.`**
Check the path for typos. Wrap paths containing spaces in quotes.

**`'...' is a file, not a directory.`**
`-p` must point to a folder, not a file.

**`pipx: command not found`**
Install pipx first (see Option 1, Step 1), then run `pipx ensurepath` and reopen your terminal.

**`git` errors during `pipx install git+...`**
pipx needs Git installed to fetch the repository. Install it from [git-scm.com](https://git-scm.com).

**`pip` is not recognized**
Use `python -m pip install .` instead.

**Permission errors during install**
Use a virtual environment (Step 3) or `pip install --user .`

**Python version error**
swx needs Python 3.7+. Download a newer version from [python.org](https://www.python.org/downloads/).

## Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a Pull Request

## Author

Created by **Davit** ([@Vatcharadze](https://github.com/Vatcharadze)).
