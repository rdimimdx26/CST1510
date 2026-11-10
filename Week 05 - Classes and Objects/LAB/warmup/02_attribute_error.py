# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# %%
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value   # stored as "amount", not "value"
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)

# The object doesn’t have an attribute called value. 
# In __init__, the value was stored as self.amount, 
# not self.value. The parameter is called value, 
# but the attribute name is whatever comes after self., which here is amount.
