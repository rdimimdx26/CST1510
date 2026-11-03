"""
A SAFER LOADER
===============
Taking Topic 3's load_records and making it survive a missing or broken file.
Run:  python 02_a_safer_loader.py
"""
# %%
def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


# --- 1. What happens right now, with no protection ---------------------------
# load_records("does_not_exist.txt") would crash with FileNotFoundError.
# Watch it happen once, on purpose, before you fix it:

try:
    load_records("does_not_exist.txt")
except FileNotFoundError:
    print("confirmed: load_records crashes on a missing file")


# --- 2. Wrap the call, not the function ---------------------------------------
# The function itself stays simple - the caller decides what "missing" means.
# %%
def safe_load_records(path):
    """Like load_records, but returns [] instead of crashing if path is missing."""
    try:
        return load_records(path)
    except FileNotFoundError:
        print(f"{path} not found - starting with an empty list")
        return []

records = safe_load_records("does_not_exist.txt")
print(records)          # [] - not a crash


# --- 3. A second real failure: a malformed line -------------------------------
# Write a bad line to a real file, then try to load it.
# %%
with open("broken_records.txt", "w") as f:
    f.write("R-001,87,100\n")
    f.write("this line is not shaped right\n")     # only one field, not three
    f.write("R-003,45,100\n")
# %%
def safe_load_records_v2(path):
    """Skips any line that isn't shaped label,value,limit instead of crashing."""
    records = []
    try:
        with open(path) as f:
            for line in f:
                try:
                    label, value, limit = line.strip().split(",")
                    records.append({"label": label, "value": float(value), "limit": float(limit)})
                except ValueError:
                    print("skipping a bad line:", line.strip())
    except FileNotFoundError:
        print(f"{path} not found - starting with an empty list")
    return records

print(safe_load_records_v2("broken_records.txt"))


# --- TRY IT ------------------------------------------------------------------
# 1. Call safe_load_records on a file you know exists - confirm it still works
#    normally, not just when something is missing.
# %%
def safe_load_records(filename):
    """Like load_records, but returns [] instead of crashing if path is missing."""
    try:
        return load_records(filename)
    except FileNotFoundError:
        print(f"{filename} not found - starting with an empty list")
        return []
records = safe_load_records("records.txt")
print(records)

# 2. Add a third bad line to broken_records.txt (e.g. a value that isn't a
#    number) and confirm it gets skipped too, not just lines with the wrong
#    number of fields.
# %% 
with open("broken_records.txt", "w") as f:
    f.write("R-001,87,100\n")
    f.write("this line is not shaped right\n")     # only one field, not three
    f.write("R-003,45,100\n")
    f.write("R-004,invalid,100\n")  # a value that isn't a number
    f.write("R-005,75,invalid\n")  # another value that isn't a number
records = safe_load_records_v2("broken_records.txt")
print(records)

# 3. In your own words: why does section 2 wrap the CALL to load_records,
#    instead of putting a try/except inside load_records itself?
# The caller decides how to handle the problem, not load_records itself and different situations need different reactions to a missing file.
# The load_records read a file and turn it into records. It doesn’t need to know what should happen when something goes wrong.
#If the try/except were inside load_records, every program using it would be forced to get [] silently, which is the silent mistake danger from the add_tax.
# By wrapping the call instead, code that wants the safe behaviour uses safe_load_records, and 
# code that wants the error to show uses load_records directly.