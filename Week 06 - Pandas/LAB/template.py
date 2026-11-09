"""
RECORD CHECK  -  my version
===========================

Name  : Rumyana Dimitrova
Lane  :  AI
Date  : 08.11.2026

Run it:   python template.py

"""
# %%
import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = None   # replace with pd.read_csv("your_file.csv")
# %%
import pandas as pd

df = pd.read_csv("records.csv")
print(df)


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".
# %%
import pandas as pd

df = pd.read_csv("records.csv")
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print(df)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
# %%
print(df)

#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.

# %%
not_ok = df[df["status"] != "OK"]
print(not_ok)

#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
# %%
import matplotlib.pyplot as plt

counts = df.groupby("status")["label"].count()
print(counts)

df.to_csv("records_report.csv", index=False)

counts.plot(kind="bar", color = "#B14CE8", title="Records per status")
plt.xlabel("Status")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()
print(df)


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
# percent = 95 ÷ 100 × 100 = 95.0
# Yes, checked : 95 is not ≥ 100, but it is ≥ 90, so the status is WARNING
#    [ ] Check you used & (not "and") if you combined more than one condition
# Yes, I did. 
#    [ ] Check every column your code refers to actually exists - watch case
# %%
print(df.columns)


