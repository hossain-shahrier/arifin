inputs = input("Enter numbers using spaces: ")

numbers_list = []
number = ""

for i in inputs:
    if i == " ":
        numbers_list.append(int(number))
        # Removes the space
        number = ""
    else:
        number = number + i

numbers_list.append(int(number))
print("List: ", numbers_list)

for i in numbers_list:
    if i % 2 == 0:
        numbers_list.remove(i)

print("Final list", numbers_list)
