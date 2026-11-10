# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# %%
class Record:
    def status(self, percent):   # this parameter should be self
        return percent

r = Record()
print(r.status(95))

# TypeError: status() takes 1 positional argument but 2 were given - Python
# passes the object (r) in automatically as the first argument, so the method
# needs self as its first parameter. Fixed by writing def status(self, percent).
