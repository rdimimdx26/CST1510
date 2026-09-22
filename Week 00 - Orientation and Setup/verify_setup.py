"""
VERIFY SETUP
==============
Run this once your install is done, before Week 1, from inside the
Week 00 folder:

    python verify_setup.py      (Windows)
    python3 verify_setup.py     (macOS)

It checks the things this module actually needs and nothing else. Every
check prints OK or MISSING - if anything is MISSING, fix that one thing and
run this again. It is safe to run as many times as you like.
"""

import shutil
import subprocess
import sys
from pathlib import Path

MIN_PYTHON = (3, 10)

REQUIRED_PACKAGES = [
    "pandas",
    "matplotlib",
    "requests",
    "bcrypt",
    "streamlit",
    "openai",
    "pytest",
]

HERE = Path(__file__).resolve().parent

failures = []


def check(label, ok, fix_hint=""):
    status = "OK" if ok else "MISSING"
    print(f"  [{status:7s}] {label}")
    if not ok:
        failures.append((label, fix_hint))


def repo_root():
    """Return the root folder of the Git repository this script is in, or None."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=HERE,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip())


print("Python version")
version_ok = sys.version_info >= MIN_PYTHON
check(
    f"Python {sys.version_info.major}.{sys.version_info.minor} (need {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+)",
    version_ok,
    "Install a current Python from https://python.org and re-run this script "
    "with that install.",
)

print("\nRequired packages")
for package in REQUIRED_PACKAGES:
    try:
        __import__(package)
        check(package, True)
    except ImportError:
        check(
            package,
            False,
            "run INSTALL.md step 7 again: python -m pip install -r requirements.txt "
            "(python3 on macOS)",
        )

print("\nGit")
git_ok = shutil.which("git") is not None
check(
    "git is on your PATH",
    git_ok,
    "Install Git from https://git-scm.com and restart your terminal / VS Code.",
)

root = repo_root() if git_ok else None
check(
    "this folder is inside your CST1510 repository",
    root is not None,
    "Move the Week 00 folder into the CST1510 folder you cloned (INSTALL.md step 5).",
)

if root is not None:
    check(
        ".gitignore file in the repository folder",
        (root / ".gitignore").is_file(),
        f"Create .gitignore in {root} (INSTALL.md step 6).",
    )

print()
if not failures:
    print("Everything checks out. See you in Week 1.")
else:
    print(f"{len(failures)} thing(s) still need fixing:\n")
    previous_hint = None
    for label, hint in failures:
        print(f"  - {label}")
        if hint and hint != previous_hint:
            print(f"    fix: {hint}")
        previous_hint = hint
    print("\nFix these, then run this file again.")
    sys.exit(1)
