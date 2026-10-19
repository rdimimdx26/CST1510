"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
# %%
label = input( " Enter a label:")
value = float(input ("Enter a value:"))
limit = float(input("Enter a limit:"))
print("Label:", label)
print("Value:", value)
print("Limit:", limit)
# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
# %%

value = 1187
limit = 1200

difference = value - limit
percent = (value/limit)*100

print("Difference:", difference)
print("Percentage:", percent)

# 3. Decide a status and store it in a variable called status.

# %% 
# Treshold
value = 1187
limit = 1200

if percent>=100:
    status = "OVER LIMIT"
else:
    status ="OK"  
print("Status:", status)
# %%
# Typical
value = 1187
limit = 1200
percent = (value / limit)*100
if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
print("Status:", status)
# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.
# %%
# Threshold
label = "Rumy's project"
value = 1187
limit = 1200
if value >= limit:
    status = "OVER LIMIT"
else:
    status = "WITHIN LIMIT"
print()
print("=" * 34)
print(f" RECORD CHECK  -  {label}")
print("=" * 34)

print("Project:", label)
print("Value:", value)
print("Limit:", limit)
print("Status:", status)

print("=" * 34)
# %%
#Typical and I have added elif 
label = "Rumy's project"
value = 1187
limit = 1200

difference = value - limit
percent = (value/limit)*100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
print()
print("=" * 34)
print(f"RECORD CHECK  -  {label}")
print("=" * 34)
print(f"Difference: {difference:>10.2f}")
print(f"Percentage: {percent:>10.2f}%")  
print("Project:", label)
print("Value:", value)
print("Limit:", limit)
print("Status:", status)

print("=" * 34)
# %%
# Excellent
over_limit_count = 0

while True:
    label = input("Enter a label (or quit): ")
    if label.lower() == "quit":
     break
    value = float(input("Enter a value:"))
    limit = float(input("Enter a limit:"))
    difference = value - limit
    percent = (value/limit)* 100
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    print()
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)

    print("Project:", label)
    print("Value:", value)
    print("Limit:", limit)
    print("Status:", status)
    print(f"Difference: {difference:>10.2f}")
    print(f"Percentage: {percent:>10.2f}%")

    print("=" * 34)

print("Total OVER LIMIT records:", over_limit_count)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds

#  Task 5 - Testing:
# Test with zero:
# Value = 1187
# Limit = 0
# Error: ZeroDivisionError: float division by zero
# Reason: Python cannot divide by zero.
# Error observed but not fixed, as instructed



