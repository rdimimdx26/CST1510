"""
RECORD CHECK  -  my version
===========================

Name  : Rumyana Dimitrova
Lane  :  AI 
Date  : 07.11.2026

Run it:   python template.py


"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
# %%
class Record:
    """A single record with a label, value and limit."""

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit


#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
# %% 
class Record:
    """A single record with a label, value and limit."""

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value as a percent of limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

print(Record("R-001", 87.0, 100.0).status())   # test
print(Record("R-002", 95.0, 100.0).status())   
print(Record("R-003", 100.0, 100.0).status())

#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.
# %%
class Record:
    over_limit_count = 0                       # class-level running total

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value as a percent of limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            Record.over_limit_count += 1       # add to the shared total
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

print(Record("R-001", 87.0, 100.0).status())   # test
print(Record("R-002", 95.0, 100.0).status())   
print(Record("R-003", 100.0, 100.0).status())
print(f"Records over limit: {Record.over_limit_count}")

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 95.0, 100.0),
]

#    Typical   : same, but now print each one's .status() as well.
# %%
records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 95.0, 100.0),
]

for r in records:
    print(r.label, r.status())
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.
# %%
def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("records.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
# %%
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"| Label:  {record.label}")
    print(f"| Value:  {record.value}")
    print(f"| Limit:  {record.limit}")
    print("=" * 34)

#    Typical   : add the result of .status().

# %%
for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"| Label:  {record.label}")
    print(f"| Value:  {record.value}")
    print(f"| Limit:  {record.limit}")
    print(f"| Status: {status}")
    print("=" * 34)

#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)
# %%
over_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"| Label:  {record.label}")
    print(f"| Value:  {record.value}")
    print(f"| Limit:  {record.limit}")
    print(f"| Status: {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_count += 1

print()
print(f"Records over limit: {over_count}")
print(f"Records over limit (variable): {over_count}")
print(f"Records over limit (class):    {Record.over_limit_count}")
# %%
class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING or OK based on value as a percent of limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"   

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records


records = load_records("records.txt")

for record in records:
    status = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"| Value:  {record.value}")
    print(f"| Limit:  {record.limit}")
    print(f"| Status: {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_count += 1

print(f"Records over limit (variable): {over_count}")
print(f"Records over limit (class):    {Record.over_limit_count}")
# %%
import os
print(os.getcwd())
print(os.listdir())
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring

