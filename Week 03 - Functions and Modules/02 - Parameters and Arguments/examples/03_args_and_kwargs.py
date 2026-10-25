"""
*args AND **kwargs
====================
Accepting an unknown number of arguments.   Run:  python 03_args_and_kwargs.py
"""

# --- 1. *args - collects extra positional arguments into a tuple -----------
# %%
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))          # 6
print(total(10, 20, 30, 40))   # 100
print(total())                 # 0 - works with none at all


# --- 2. *args really is just a tuple - loop it, index it -------------------
# %%
def describe(*items):
    print(f"{len(items)} item(s): {items}")
    for item in items:
        print(" -", item)

describe("router", "switch", "firewall")


# --- 3. **kwargs - collects extra keyword arguments into a dict ------------
# %%
def configure(**settings):
    for key, value in settings.items():
        print(f"{key} = {value}")

configure(host="10.0.0.1", port=8080, ssl=True)


# --- 4. Mixing named parameters with *args and **kwargs ---------------------
# Order matters: normal params, then *args, then **kwargs.
# %%
def connect(host, *extra_hosts, **options):
    print("primary host:", host)
    if extra_hosts:
        print("also connecting to:", extra_hosts)
    for key, value in options.items():
        print(f"  option {key} = {value}")

connect("10.0.0.1")
connect("10.0.0.1", "10.0.0.2", "10.0.0.3", timeout=5, retries=3)


# --- WATCH OUT: *args is a tuple, not separate variables --------------------
# numbers = total(1, 2, 3)  does NOT give you numbers[0], numbers[1], numbers[2]
# as three separate variables - inside total(), *numbers IS one tuple (1, 2, 3).


# --- TRY IT ------------------------------------------------------------------
# 1. Write average(*values) that returns the mean of however many numbers it
#    gets. Call it with 3 numbers, then with 6.
# %%
def average(*values):
    return sum(values)/len(values)
print(average(2,7,9))
print(average(20,30,40,50,60,70))

      
# 2. Write log_event(event, **details) that prints the event name, then one
#    line per extra detail passed in as a keyword argument.
# %% 
def log_event(event, **details):
    print("Event:", event)
    for key, value in details.items():    # With .items() we get each (key, value) pair, which we unpack into two variables:
     print(f"{key}:{value}")           # for key, value in details.items():
log_event("login", user = "Rumyana")  # Without.items()Looping over a dictionary directly gives only the keys
 
# 3. Call connect() from section 4 with a host and three keyword options of
#    your own choosing - predict the output before running it.
# %%
def connect(main_host, *extra_hosts, **options ):
    print("main host:",main_host)
    if extra_hosts:
        print("also connecting to:", extra_hosts)
    for key, value in options.items():
        print(f"options {key},{value}")

connect("abv.bg") 
connect("abv.bg", "outlook", "mail.co.uk", timeout=10, secure=True)      
              


# %%
def add_users(main_user, *extra_users, **options ):
    print("main user:", main_user)
    if extra_users:
        print("also adding:", extra_users)
    for key, value in options.items():
        print(f"  options {key} , {value} ")
     
add_users("Rumyana", Anna="new user", Alex="student", assessment= "score", course="CST1510")        
# %%
def main_dish("dish", *sides, **extras):
    print("main dish", dish)
    if sides:
        print("sides:", sides)
        for key, value in extras.items():
            print(f " {key} = {value}")
main_dish("beef Bourguignon", "pasta", "omlet", size = "to share", spicy=False)# It will print main dish: beef Bourgunion, extras: pasta, extras: omlet, extra size to share, extras spicy.  
       


# %%
