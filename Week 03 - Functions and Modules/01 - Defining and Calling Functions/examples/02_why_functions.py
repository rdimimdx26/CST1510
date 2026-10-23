"""
WHY FUNCTIONS
=============
The same job, with and without one.   Run:  python 02_why_functions.py
"""

# --- 1. Without a function - repeated, and easy to get out of sync ----------
# %%
value1, limit1 = 87, 100
print(f"{(value1 / limit1) * 100:.1f} %")
# %%
value2, limit2 = 120, 100
print(f"{(value2 / limit2) * 100:.1f} %")
# %%
value3, limit3 = 45, 100
print(f"{(value3 / limit3) * 100:.1f} %")

# Fix a mistake in that formula and you have to fix it three times.
# Miss one, and two records are now calculated differently to the third.
# %%
def percent_of_limit(value,limit):
    return (value/limit)* 100

print(f"{percent_of_limit(87,100):.1f}%")
print(f"{percent_of_limit(120,100):.1f}%")
print(f"{percent_of_limit(45,100):.1f}%")




# --- 2. With a function - one place, one truth -------------------------------
# %%
def percent_of(part, total):
    return (part / total) * 100

print(f"{percent_of(87, 100):.1f} %")
print(f"{percent_of(120, 100):.1f} %")
print(f"{percent_of(45, 100):.1f} %")

# Fix the formula once, inside percent_of, and every call is fixed.
# Miss one, and two records are now culculated differently to the third.

# --- 3. A good function does one job -----------------------------------------
# percent_of only calculates. It does not print, does not ask for input,
# does not decide a status. Each of those would be its own function.
# %%
def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# Now they can be combined, or used completely separately:
print(status_of(percent_of(87, 100)))
print(status_of(95))                    # status_of doesn't care where 95 came from


# --- TRY IT ------------------------------------------------------------------
# 1. Name one reason percent_of and status_of are two functions and not one.
# 2. Write a function is_valid_percent(p) that returns True if p is between
#    0 and 100 inclusive. Use it to check percent_of(87, 100).

# %%
# 1. Name one reason percent_of and status_of are two functions and not one.
# percent_of calculates a number and status_of decides a label. Both can be used and fixed or changed separetly, without affecting the other.

# 2. Write a function is_valid_percent(p) that returns True if p is between
#    0 and 100 inclusive. Use it to check percent_of(87, 100).
# %%
def is_valid_percent(value,limit): #Remember: names go in the brackets when you define a function with def
    return (value/limit)*100

def is_valid_percent(p):
    return 0<=p<=100
result=percent_of(87,100) # and real values go in when you call it.
print(result, is_valid_percent(result))
    


# %%
