"""
.replace(), .startswith(), .endswith(), .count()
===================================================
Changing text, and checking its edges.
Run:  python 02_replace_startswith_endswith.py
"""

# --- 1. .replace() - swap every occurrence ------------------------------
# %%
hostname = "srv_01_east"
print(hostname.replace("_", "-"))     # srv-01-east - every underscore


# --- 2. .replace() only replaces exact matches --------------------------

print("SRV_01".replace("_", "-"))     # SRV-01 - case-sensitive, like everything else


# --- 3. .startswith() and .endswith() -----------------------------------
# Very common for filtering - log level prefixes, file extensions, IDs.

line = "ERROR: connection refused"
print(line.startswith("ERROR"))     # True
print(line.startswith("WARN"))       # False

filename = "backup_2026.csv"
print(filename.endswith(".csv"))     # True
print(filename.endswith(".txt"))      # False


# --- 4. .count() - how many times something appears -----------------------

log = "retry retry retry failed"
print(log.count("retry"))     # 3


# --- 5. Combining these to filter a batch of lines --------------------------

lines = ["ERROR: disk full", "INFO: backup complete", "ERROR: timeout"]

for line in lines:
    if line.startswith("ERROR"):
        print("Needs attention:", line)


# --- 6. Same idea, three fields ---------------------------------------------

survey_row = "Age: 21, Notes: missing"
print("missing" in survey_row.lower())          # AI / Data Science

log_line = "FAILED login from 10.0.0.5"
print(log_line.startswith("FAILED"))            # Cyber Security

for name in ["app.log", "app.csv"]:
    if name.endswith(".log"):                    # IT
        print(name, "is worth checking")


# --- TRY IT ------------------------------------------------------------------
# 1. Replace every "-" with "_" in "srv-01-east".
# %%
hostname = "srv-01-east"
print(hostname.replace("-", "_"))

# 2. Given a list of filenames, print only the ones ending in ".log".
# %%
filenames = ["server.log", "report.csv", "update.log", "file.txt", "access.log"]

for name in filenames:
    if name.endswith(".log"):
        print(name)
# 3. 
# %%

log = "FAILED login. Retry failed. Disk check OK. Backup Failed."
print(log.lower().count("failed"))
# %%
