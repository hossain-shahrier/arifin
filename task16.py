
numbers_list = []

for i in range(7):
    num = int(input("Enter a number: "))
    numbers_list.append(num)

largest = numbers_list[0]
second_largest = numbers_list[1]
largest_index = 0
second_largest_index = 1
#  [7, 13, 2, 10, 6, -11, 0]
for i in range( len(numbers_list)):
    if numbers_list[i] > largest:
        second_largest = largest
        second_largest_index = largest_index
        largest = numbers_list[i]
        largest_index = i
    elif numbers_list[i] > second_largest:
        second_largest = numbers_list[i]
        second_largest_index = i

print("Second largest number is", second_largest, "and its index position on the list is", second_largest_index)