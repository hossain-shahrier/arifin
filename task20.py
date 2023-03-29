"""
Write a python program to take a list as a string input from the user and print it back to the user as a list.
Please look at the examples below for clarification.
[Must use string split() and strip() functions]
================================================================
Sample Input 2: '[1,      2   ,            3, 50, 4]'
Sample Output 2:
Original data: [1,      2   ,            3, 50, 4]
After removing square brackets: 1,      2   ,            3, 50, 4
Numbers in string format with extra white spaces: ['1', '      2   ', '            3', '50', '4']
Final data (numbers in list format): [1, 2, 3, 50, 4]

"""
input_str = input("Enter a list as a string: ")
original = input_str
input_str = input_str.strip('[]')

num_strs = input_str.split(',')
new_num_str = num_strs

new_list = []

for num in num_strs:
    stripped_num = num.strip()
    new_list.append(stripped_num)
num_strs = new_list

new_list = []
for num in num_strs:
    int_num = int(num)
    new_list.append(int_num)
num_list = new_list

# Print original input, number strings with extra whitespace, and final output

print("Original data: " + original)
print("After removing square brackets: " + input_str)
print("Numbers in string format with extra white spaces: ", new_num_str)
print("Final data (numbers in list format): " + str(num_list))
