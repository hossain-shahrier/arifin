"""Write a python program that will take a number as an input and check whether the number is Awesome or not.
If the number is Awesome, it prints True. Otherwise, False.
Awesome number: a number where every digit is less than its immediate left digit is called an Awesome number.
A single-digit number cannot be an awesome number(e.g. 5421 is an Awesome number.)
"""

user_number = []

number = input("Enter your number: ")

awesome = True

for i in range(1, len(number)):
    if int(number[i]) >= int(number[i-1]):
        awesome = False
        break
print(awesome)
