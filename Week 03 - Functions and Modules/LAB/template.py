"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI
Date  :

Run it:   python template.py

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here

#Threshold:
# %%
def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

print(status_of(100))
print(status_of(90))
print(status_of(75))


# Typical and above:

def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent
result = check(1187, 1200)

print(result)


# Excellent: 

def print_report(label, value, limit, difference, percent, status):
     """Print a formatted report of the record."""
     
     print("=" * 34)
     print(f"RECORD CHECK - {label}")
     print("=" * 34)
     print("Value:", value)
     print("Limit:", limit)
     print(f"Difference: {difference:>10.2f}")
     print(f"Percentage: {percent:>10.2f}%")
     print("Status:", status)
     print("=" * 34)

label = input("Enter a label: ")
value = float(input("Enter a value: "))
limit = float(input("Enter a limit: "))
difference, percent = check(value, limit)
status = status_of(percent)

print_report(label, value, limit, difference, percent, status)
# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

#label = ""      # replace with an input() call
#value = 0.0     # replace with an input() call, converted
#limit = 0.0     # replace with an input() call, converted

label = input("Enter a name or hostname: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))

print(label)
print(value)
print(limit)

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.

# %%  

difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)

    
#    Typical   : call check() to get the difference and percentage instead.

#difference = 0.0   # replace with your code
#percent = 0.0       # replace with your code
#status = ""          # replace with your code

difference, percent = check(value, limit)
status = status_of(percent)

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"| Label:  {label}")
print(f"| Value:  {value}")
print(f"| Limit:  {limit}")
print(f"| Status: {status}")
print(f"Difference : {difference:>10.2f}")
print(f"Percent    : {percent:>10.2f}%")

print("=" * 34)



# %%

def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report of the record."""
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)
    print("Value:", value)
    print("Limit:", limit)
    print(f"Difference: {difference:>10.2f}")
    print(f"Percentage: {percent:>10.2f}%")
    print("Status:", status)
    print("=" * 34) 

over_count = 0

while True:

    label = input("Enter a name or hostname (or 'quit' to stop): ")
    if label.lower() == "quit":
        break
    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    difference = value - limit
    percent = (value / limit) * 100
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count += 1

print(f"\nRecords over limit: {over_count}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it

# %%
