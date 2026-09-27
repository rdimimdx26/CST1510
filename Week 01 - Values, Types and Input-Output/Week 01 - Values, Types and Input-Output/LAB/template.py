"""
RECORD CHECK  -  my version
===========================

Name  : Rumyana Dimitrova
Lane  :  AI    
Date  : 26.09.2026
Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#    Remember: input() always gives back text.

label = input("Enter a label: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))


# ================================================================== PROCESS
# 

difference = first - second
percent = (first / second) * 100





# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"First:      {first:>10.2f}") 
print(f"Second:     {second:>10.2f}")
print(f"Difference: {difference:>+10.2f}")
print(f"Percent:    {percent:>+10.2f} %")

print("=" * 34)
print(f"Total:       {first + second:>10.2f}")
print("Checked by: Rumyana Dimitrova")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
