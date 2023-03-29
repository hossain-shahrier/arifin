"""Write a Python program that takes a list from the user. Then find the first even and first odd number in
the list.
"""
input_list = []

input_count = int(input("How many inputs do you want to take:"))
first_even = None
first_odd = None
for i in range(input_count):
    user_input = int(input("Enter your number:"))
    input_list.append(user_input)

for i in input_list:
    if i % 2 == 0:
        first_even = i
        break

for i in input_list:
    if i % 2 == 1:
        first_odd = i
        break

if first_even is not None:
    print("The first even number in the list is:", first_even)
else:
    print("Even, not found")

if first_odd is not None:
    print("The first odd number in the list is:", first_odd)
else:
    print("Odd, not found")