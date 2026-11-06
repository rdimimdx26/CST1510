"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI
Date  :

Run it:   python template.py

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
# %%
def check_record(value, limit):
    """Checking if value exceeds the limit and returns difference, percent, and status."""
    difference = value - limit
    percent = (value / limit) * 100
    if percent > 100:
        status = "OVER LIMIT"
    elif percent >= 85:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(value, limit, difference, percent, status):
    """Print a report showing the value, limit, difference and status."""

    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percentage: {percent:.1f}%")
    print(f"Status: {status}")




# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job

# %%
