list1_str = input("Enter the first list separated by spaces ans commas: ")
new_list1 = []
split_list1 = list1_str.split()
for elem in split_list1:
    new_list1.append(elem)
list1 = new_list1

list2_str = input("Enter the first list separated by spaces ans commas: ")
new_list2 = []
split_list2 = list2_str.split()
for elem in split_list2:
    new_list2.append(elem)
list2 = new_list2

common_list = []

for elem in list1:
    if elem in list2 and elem not in common_list:
        common_list.append(elem)

print("Common elements:", common_list)
