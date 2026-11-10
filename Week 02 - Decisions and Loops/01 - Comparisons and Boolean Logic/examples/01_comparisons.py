"""
COMPARISONS
===========
Six operators, one job each: ask a question, get True or False.   Run:  python 01_comparisons.py
"""

# --- 1. The six operators ---------------------------------------------------

value = 23.7
limit = 20

print(value == limit)     # False  - equal to?
print(value != limit)     # True   - not equal to?
print(value >  limit)     # True   - greater than?
print(value <  limit)     # False  - less than?
print(value >= limit)     # True   - greater than or equal to?
print(value <= limit)     # False  - less than or equal to?


# --- 2. The result is always a bool -----------------------------------------

is_over = value > limit

print(is_over)            # True
print(type(is_over))      # <class 'bool'>


# --- 3. = stores, == asks ----------------------------------------------------
# This is the single most common slip this week.

limit = 20          # =  : "limit now holds 20"
print(limit == 20)  # == : "does limit hold 20?"  -> True

# limit = 20 == True and limit == 20 look similar. They are not the same
# operation. Read = as "gets", == as "is this the same as".


# --- 4. Comparing different types -------------------------------------------
# A number and its text version are never equal, no matter what they look like.

print(20 == "20")     # False - int vs str, never equal
print(20 == 20.0)     # True  - int vs float, numbers still compare fairly


# --- TRY IT ------------------------------------------------------------------
# 1. Set attempts = 4 and max_attempts = 3. Print whether attempts is over the max.
# %%
attempts = 4
max_attempts = 3

print(attempts > max_attempts)

# 2. Predict, then check: 90 >= 90   and   90 > 90
# 90 >= 90 gives True, because >= means “greater than or equal to”, and 90 is equal to 90
# 90 > 90 gives False, because > means “strictly greater than”, and 90 isn’t greater than itself

# 3. Explain out loud why "3" == 3 is False.
#"3" == 3 is False because the two values are different types. 
# "3" (in quotes) is a string, the text character “3”. 
# 3 (no quotes) is an integer, the number three. 
# Python doesn’t automatically convert one type into the other when comparing with ==, so a piece of text is never equal to a number, 
# even if they look the same when printed.
# %%
