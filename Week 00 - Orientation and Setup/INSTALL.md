# Setting up for CST1510

Do these steps in order, once, before Week 1. Each step ends with a quick
check so you know it worked before moving on.

> **Prefer a visual version?** The
> [Setup Guide](https://anna29.github.io/CST1510/setup-guide.html) covers
> installing, and the
> [Git & GitHub Guide](https://anna29.github.io/CST1510/git-and-github-guide.html)
> covers the weekly routine. This page is the text version of both.

**Windows or Mac?** Commands are the same on both, except Python:
Windows uses `python`, macOS uses `python3`.

**Opening a terminal:** Windows: Start menu → type `PowerShell`.
macOS: `Cmd + Space` → type `Terminal`.

---

## 1. Install Python

```
python --version      # Windows
python3 --version     # macOS
```

If this shows **Python 3.10 or higher**, go to step 2. Otherwise install
Python from [python.org/downloads](https://www.python.org/downloads/).

- **Windows:** on the first screen, tick **"Add python.exe to PATH"**. If you
  miss it, nothing later works and you'll need to reinstall.
- Close and reopen the terminal, then run the check again.

## 2. Install VS Code

Install from [code.visualstudio.com](https://code.visualstudio.com/). Then in
VS Code open Extensions (`Ctrl + Shift + X`, or `Cmd + Shift + X` on Mac) and
install **Python** and **Jupyter**, both by Microsoft.

## 3. Install Git and create a GitHub account

Install Git from [git-scm.com/downloads](https://git-scm.com/downloads),
accepting the defaults. (On a Mac, running `git --version` may offer to
install it for you: accept.) Create a free account at
[github.com](https://github.com/) if you don't have one.

Then tell Git who you are, using the email from your GitHub account:

```
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Check:** `git --version` prints a version number.

## 4. Create and clone your repository

Your repository holds all your work for the whole module, Week 0 to Week 12.

1. On GitHub, click **+** (top right) → **New repository**.
2. Name it `CST1510`, choose **Private**, and tick **Add a README file**.
3. Click **Create repository**, then click the green **Code** button and copy
   the HTTPS URL.
4. In a terminal:

```
cd Documents
git clone https://github.com/YOUR-USERNAME/CST1510.git
```

This creates the folder `Documents/CST1510`, already linked to GitHub.
Don't create the folder yourself first.

Because the repository is private, Git asks you to sign in. On Windows a
browser window opens. On a Mac, enter your GitHub username, and when it asks
for a password paste a **personal access token** (see the table at the end).

**Check:** `Documents/CST1510` exists and contains `README.md`.

## 5. Put this week's folder inside your repository

Move this whole `Week 00 - Orientation and Setup` folder into
`Documents/CST1510`. Every week from now on, the new week's folder goes in
there too.

Then open the repository in VS Code: **File → Open Folder** → `CST1510`.
Open a terminal inside VS Code with **Terminal → New Terminal**. It starts
in the right folder, so use this terminal from now on.

## 6. Add a `.gitignore` file

This tells Git which files never to upload. In VS Code, create a new file in
the `CST1510` folder itself (not inside a week folder), name it `.gitignore`
(starting with a dot), paste this in and save:

```
__pycache__/
.ipynb_checkpoints/
.DS_Store
.env
```

## 7. Install the module's packages

In the VS Code terminal:

```
cd "Week 00 - Orientation and Setup"
python -m pip install -r requirements.txt       # Windows
python3 -m pip install -r requirements.txt      # macOS
```

This installs everything used across all 12 weeks, so you won't need to
install anything most weeks.

## 8. Check everything worked

Still inside the Week 00 folder:

```
python verify_setup.py       # Windows
python3 verify_setup.py      # macOS
```

Every line should say `OK`. If something says `MISSING`, the line under it
tells you the fix. Do that one thing and run the script again.

## 9. Make your first push

Go back up to the repository folder and save everything to GitHub:

```
cd ..
git add .
git commit -m "Week 0 setup"
git push
```

Open your repository on GitHub and check you can see the Week 00 folder and
`.gitignore`. Then go to **Settings → Collaborators → Add people** and add
your lecturer (`anna29`), so the repository link you submit can be opened.

---

## Every week from now on

At the end of each lab, in the VS Code terminal (inside `CST1510`):

```
git status
git add .
git commit -m "Week N lab and mini-project"
git push
```

Change `N` to the week number, then check the files are on GitHub. Anything
you want to keep must be inside the `CST1510` folder, or it won't be
uploaded.

---

## If something won't cooperate

| Problem | Fix |
|---|---|
| `python` or `python3`: command not found | Reinstall Python (Windows: tick "Add python.exe to PATH"), then reopen the terminal |
| Typing `python3` on Windows opens the Microsoft Store | On Windows, use `python`, not `python3` |
| `No module named pip` or pip errors | Use the exact `python -m pip ...` / `python3 -m pip ...` command from step 7 |
| `externally-managed-environment` (macOS) | You're using a different Python (e.g. Homebrew's). Install Python from python.org and run step 7 again |
| `cd Documents` fails (Windows) | Your Documents folder may be in OneDrive: try `cd ~\OneDrive\Documents` |
| `git`: command not found | Close and reopen the terminal (and VS Code) after installing Git |
| Git asks for a password and rejects it | GitHub needs a **personal access token**, not your password. On GitHub: Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token, tick **repo**, copy it and paste it as the password |
| `fatal: not a git repository` | You're not inside the `CST1510` folder. Open it in VS Code and use its terminal |
| `nothing added to commit` or `no changes added to commit` | You skipped `git add .` |
| `rejected` … `fetch first` when pushing | GitHub has a change you don't (e.g. you edited on the website). Run `git pull`, then `git push` |
| `'...' is not a git command` | Check the spelling, e.g. `config` not `confir` |
| `verify_setup.py` says the folder is not inside your repository | Move the Week 00 folder into `Documents/CST1510` (step 5) |
| No Python kernel for a `.ipynb` notebook | Install the Jupyter extension (step 2), reopen the notebook and click **Select Kernel** (top right) |

Still stuck? Flag it in the session. Getting set up is what Week 0 is for.
