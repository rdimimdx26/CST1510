"""
RECORD CHECK  -  my version
===========================

Name  :Rumyana Dimitrova
Lane  :  AI
Date  :06.11.2026

Run it:   python template.py
"""
# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
# %%
def check_record(value, limit):
    """Return the difference, percent and status for a value against its limit."""  

    difference = value - limit
    percent = (value / limit) * 100
    if percent > 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(value, limit, difference, percent, status):
    """Print a report showing the value, limit, difference, percent and status."""    
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference:.2f}")
    print(f"Percentage: {percent:.1f}%")
    print(f"Status: {status}")

difference, percent, status = check_record(87, 100)  # test
print_report(87, 100, difference, percent, status)   # test


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.

records = [{"label": "Server1", "value": 95, "limit": 100},
           {"label": "Server2", "value": 87, "limit": 100},
           {"label": "Server3", "value": 80, "limit": 100}]
           
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
# %%
def load_records(path):
    records = []
    with open (path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append ({"label": label.strip(),
                             "value": float(value),
                             "limit": float(limit),})   # trailing comma, and it’s optional. Python allows a comma after the last item in a dictionary, list or function call, and ignores it. Adding an item later is easier. exception is a tuple with a single item. There, the comma does matter.
            return records
        records = load_records ("records.txt")

#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.


records = load_records("records.txt")

def save_results(path, results):
    """Write each record's label and status to a file, one per line."""
    with open(path, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
results = []                                                                                      # empty list before the loop starts. It’s where the label and status of each record get collected.It works the same way as over_count = 0

for record in records:                                                                            # takes each dictionary from the list in turn 

    difference, percent, status = check_record(record["value"], record["limit"])                  # check_record returns three values, which are unpacked into three variables.
    # record["label"], record["value"] etc. pull each item out of the dictionary by its key                                                                                      
    print_report(record["label"], record["value"], record["limit"], difference, percent, status)  
    results.append((record["label"], status))                                                     # remembers the label and status for the file

save_results("results.txt", results)                                                              # # save_results is not indented, so it runs once, after the loop has finished   

                                             

def print_report(label, value, limit, difference, percent, status):
    """Print a report showing the label, value, limit, difference, percent and status."""
    print(f"Record: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference:.2f}")
    print(f"Percentage: {percent:.1f}%")
    print(f"Status: {status}")
    print()

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
