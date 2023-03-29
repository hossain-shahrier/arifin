"""
Write a Python program that takes a single string as an input from the user where few numbers are separated by commas.
Now, make a list with the numbers of the given string.
Then your task is to remove multiple occurrences of any number
and then finally print the list without any duplicate values.
Hint (1): For obtaining the numbers from the string, use split(). For cleaning the data, use strip().
Hint (2): You may create a third list to store the results. You can use membership operators (in, not in) to make sure no duplicates are added.
===================================================================
Sample Input 1:
0, 0, 1, 2, 3, 4,      4, 5, 6, 6, 6,      7, 8, 9, 4,         4
Sample Output 1:
Given numbers in list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
List without any duplicate values: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


input_str = input("Enter a string with numbers separated by commas: ")
num_strs = input_str.split(",")

num_list = []
for num in num_strs:
    stripped_num = num.strip()
    num_list.append(stripped_num)

unique_nums = []

for num_str in num_list:
    num = int(num_str)
    if num not in unique_nums:
        unique_nums.append(num)

print("List without duplicate values:", unique_nums)
