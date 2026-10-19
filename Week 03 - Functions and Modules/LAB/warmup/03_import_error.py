# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# %%
import maths

print(maths.sqrt(16))

# %%
# Test: 
#ModuleNotFoundError: No module named 'maths'
#Python's built-in module is called math, not maths.
# %%
# The code fixed:
import math

print(math.sqrt(16))
#Output 4.0
# %%
