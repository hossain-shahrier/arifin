num_list = []

for i in range(5):
    num = int(input("Enter a number: "))
    num_list.append(num)

smallest = num_list[0]
largest = num_list[0]
smallest_index = 0
largest_index = 0

for i in range(len(num_list)):
    if num_list[i] < smallest:
        smallest = num_list[i]
        smallest_index = i
    elif num_list[i] > largest:
        largest = num_list[i]
        largest_index = i

print("Smallest number is", smallest, "and its index position on the list is", smallest_index)
print("Largest number is", largest, "and its index position on the list is", largest_index)