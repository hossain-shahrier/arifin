numbers = input("Enter numbers separated by commas: ")
numbers_list = numbers.split(", ")

magic_nums = []
non_magic_nums = []

for num in numbers_list:
    even_sum = 0
    odd_sum = 0
    for i in range(len(num)):
        if i % 2 == 0:
            even_sum += int(num[i])
        else:
            odd_sum += int(num[i])
    if even_sum == odd_sum:
        magic_nums.append(int(num))
    else:
        non_magic_nums.append(int(num))

result = (tuple(magic_nums), tuple(non_magic_nums))
print(result)
