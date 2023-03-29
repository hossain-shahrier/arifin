"""
Write a Python program that takes two lists as an input from the user. Then print a new list with the common elements of both the input lists.
Hint: You may need to create a third list to store the results. You can use membership operators (in, not in) to make sure similar elements are added.
===================================================================
Sample Input 1:
A, B, C, D
C, E, F, B
Sample Output 1:
['C', 'B']
"""

list1_str = input("Enter the first list separated by spaces ans commas: ")
new_list1 = []
split_list1 = list1_str.split(", ")
for elem in split_list1:
    new_list1.append(elem)
list1 = new_list1

list2_str = input("Enter the first list separated by spaces ans commas: ")
new_list2 = []
split_list2 = list2_str.split(", ")
for elem in split_list2:
    new_list2.append(elem)
list2 = new_list2

common_list = []

for elem in list1:
    if elem in list2 and elem not in common_list:
        common_list.append(elem)

print("Common elements:", common_list)
