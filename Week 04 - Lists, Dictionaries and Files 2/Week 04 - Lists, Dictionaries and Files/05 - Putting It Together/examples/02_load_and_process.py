"""
LOAD AND PROCESS
=================
The full shape: read a file, build a list of dicts, process each one.
This is exactly what this week's DEMO does.
Run:  python 02_load_and_process.py
(needs sample_records.txt in the same folder)
"""
# %%
def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


# --- 1. Loading turns a file into a list of dicts ---------------------------

records = load_records("sample_records.txt")
print(records)
print(len(records), "records loaded")


# --- 2. Processing each one --------------------------------------------------

for record in records:
    percent = (record["value"] / record["limit"]) * 100
    status = "OVER LIMIT" if percent >= 100 else "OK"
    print(f"{record['label']}: {status}")


# --- 3. Building a summary as you go -----------------------------------------

over_limit_count = 0

for record in records:
    percent = (record["value"] / record["limit"]) * 100
    if percent >= 100:
        over_limit_count += 1

print(f"{over_limit_count} of {len(records)} were over limit")


# --- TRY IT ------------------------------------------------------------------
# 1. Add a WARNING tier (90% or more) to the loop in section 2.
for record in records:
    percent = (record["value"] / record["limit"]) * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    print(f"{record['label']}: {status}")

# 2. Write your own load_records-style function for a file with a different
#    number of fields per line.
# %%
with open("records_with_status.txt", "w") as f:
    f.write("R-001,87,100,OK\n")
    f.write("R-002,120,100,OVER LIMIT\n")
    f.write("R-003,45,100,OK\n")

def load_records_with_status(path):
    """Read label,value,limit,status lines from a file and return a list of dicts with status."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit, status = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
                "status": status
            })
    records = load_records_with_status("records_with_status.txt")
for record in records:
    print(record)
# 3. Change the loop in section 3 to also count how many were exactly OK.

# %%
records = load_records("records.txt")

over_limit_count = 0
ok_count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    if status == "OVER LIMIT":
        over_limit_count += 1
    if status == "OK":
        ok_count += 1

print(f"Checked {len(records)} records. {over_limit_count} were over limit, {ok_count} were OK.")

# %%
