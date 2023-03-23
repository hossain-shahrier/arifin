input_str = input("Enter a list as a string: ")

input_str = input_str.strip('[]')

num_strs = input_str.split(',')

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
print("Original data: " + input_str)
print("After removing square brackets: " + ", ".join(num_strs))
print("Numbers in string format with extra white spaces: " + str(num_strs))
print("Final data (numbers in list format): " + str(num_list))
