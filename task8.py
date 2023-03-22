list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

temp = []
# new_list = [x for x in list_one + list_two if x % 2 == 0]

for x in list_one + list_two:
    if x % 2 == 0:
        temp.append(x)

print(temp)
