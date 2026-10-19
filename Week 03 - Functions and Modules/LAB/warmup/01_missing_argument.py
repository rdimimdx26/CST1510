# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# %%
def status_of(percent, warning_at):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95))

# Test: 
#The code is missing another argument (number).
#TypeError: status_of() missing 1 required positional argument: 'warning_at
# %%
# The code fixed:
def status_of(percent, warning_at):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95, 90))
#Output: WARNING

# %%
def status_of(percent, warning_at):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95, 97))
#status_of is to decide the status of a percentage.
It doesn't calculate a percentage. It compares an existing percentage against two thresholds.
