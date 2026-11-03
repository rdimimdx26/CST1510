# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
# %%
with open("records.txt", "w") as f:
    f.write("R-001,87,100\n")
    f.write("R-002,120,100\n")
    f.write("R-003,45,100\n")
with open("records.txt", "r") as f:         
    print(f.read())


# %%
