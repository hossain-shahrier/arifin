numbers = "7, 13, 2, 10, 6, -11, 0"
numbers_list = numbers.split(",")

largest_number = int(numbers_list[0])
largest_number_index = 0

for i in range(1, len(numbers_list)):
    if int(numbers_list[i]) > largest_number:
        largest_number = int(numbers_list[i])
        largest_number_index = i
print("The largest number is", largest_number, "and its index position is", largest_number_index)