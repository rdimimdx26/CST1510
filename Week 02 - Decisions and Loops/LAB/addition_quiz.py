# """
# this task is to create a simple addition quiz that asks the user to add two numbers together.
#  The program will check if the user's answer is correct and provide feedback accordingly.
# """

# '''
# while True: 
#     num1= 4
#     num2= 5

#     answer =int(input(f"What is {num1} + {num2}?"))

#     if answer == num1 + num2:
#         print("Correct!")
#         break
#     else:
#         print ("Try again!")
# '''

# %%

import random

num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

while True:
    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Try again!")

# %%
print(ord("a"))
print(ord("b"))
print(ord("A"))

print(ord("А"))
print(ord("Б"))
print(ord("а"))
# %%
