inputs = input("Enter numbers separated by commas: ")
input_list = inputs.split(",")
numbers_list = []

for number in input_list:
    numbers_list.append(int(number))
print("Input List",numbers_list)

# Remove duplicates from the list
no_duplicates = []
for number in numbers_list:
    if number not in no_duplicates:
        no_duplicates.append(number)

print("Modified List: ", no_duplicates)
