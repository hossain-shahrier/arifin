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
