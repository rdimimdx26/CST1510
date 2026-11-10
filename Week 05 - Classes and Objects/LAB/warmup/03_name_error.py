# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# %%
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        return "OVER LIMIT" if self.value > self.limit else "OK"

r = Record("R-001", 120.0, 100.0)
print(r.status())

# Status is a method: it belongs to the Record class, 
# so it lives on the object. On its own, 
# status() makes Python look for a normal function called status outside the class, and there isn’t one.

# %%
