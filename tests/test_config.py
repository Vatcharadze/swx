import sys
from pathlib import Path

from swx.config import get_dir_path


def test_get_dir_path(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["swx", "-p", "."])

    result = get_dir_path()

    assert result == Path(".")