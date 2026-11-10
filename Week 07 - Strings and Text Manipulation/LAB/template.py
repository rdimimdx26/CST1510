"""
RECORD CHECK  -  my version
===========================

Name  : Rumyana Dimitrova
Lane  :  AI 
Date  : 10.11.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
# %%
def parse_line(raw_line):
    """Clean and parse one raw, messy line into a dict."""
    result = {}
    for piece in raw_line.split(","):
        if "=" not in piece:
            result["Survey"] = piece.strip().lower()
        else:
            key, value = piece.split("=")
            result[key.strip().lower()] = float(value.strip())

    return result


#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.
# %%

def status_of(rating, low_at=2):
    """Return FLAGGED for a low rating (low_at or below), otherwise OK."""
    if rating <= low_at:
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.
# %%
raw_records = []   

with open("messy_records.txt") as f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        raw_records.append(line)

print(raw_records)

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
# %%
for raw in raw_records:
    record = parse_line(raw)
    print(record)

#    Typical   : also call status_of(...) for each, print it alongside.
# %%
for raw in raw_records:
    record = parse_line(raw)
    print(record, status_of(record["rating"]))

#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

# %%
flagged_count = 0

for raw in raw_records:
    record = parse_line(raw)
    status = status_of(record["rating"])
    print(record, status)

    if status == "FLAGGED":
        flagged_count += 1

print(f"{len(raw_records)} records, {flagged_count} flagged")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
# Done
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
# ValueError: invalid literal for int() with base 10: 'four
#    [ ] Check every function does one job, with a docstring
# Present


