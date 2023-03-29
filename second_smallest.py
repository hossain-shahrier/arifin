numbers_list = []

for i in range(7):
    inputs = int(input("Enter your number: "))
    numbers_list.append(inputs)

smallest = numbers_list[0]
second_smallest = numbers_list[1]
smallest_index = 0
second_smallest_index = 1

#  [7, 13, 2, 10, 6, -11, 0]
if second_smallest < smallest:
    smallest, second_smallest = second_smallest, smallest

for i in range(2, len(numbers_list)):
    if numbers_list[i] < smallest:
        second_smallest = smallest
        smallest = numbers_list[i]
        smallest_index = i
    elif numbers_list[i] < second_smallest:
        second_smallest = numbers_list[i]
        second_smallest_index = i
print("The second smallest number in the list is:", second_smallest, " and index is ", second_smallest_index)
