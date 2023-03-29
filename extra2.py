"""
Write a Python program to reverse strings in a given list of string values without using reverse() or
reversed().
"""

string_list = ['Red', 'Green', 'Blue', 'White', 'Black']
reversed_list = []

for string in string_list:
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    reversed_list.append(reversed_string)

print(reversed_list)
