number_list = []

for i in range(7):
    number_input = int(input("Enter a number: "))
    number_list.append(number_input)

# [7 6 13 19 18 23 25]

largest_number = number_list[0]
second_largest_number = number_list[0]
largest_number_index = 0

for number in range(len(number_list)):
    if number_list[number] > largest_number:
        second_largest_number = largest_number
        largest_number = number_list[number]
        largest_number_index = number
    elif number_list[number] > second_largest_number and number_list[number] != largest_number:
        second_largest_number = number_list[number]
        largest_number_index = number

print("Second largest number is", second_largest_number, "and its index position on the list is", largest_number_index)
