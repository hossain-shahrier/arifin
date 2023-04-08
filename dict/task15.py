tuple_list = [(2, 3), (4, 5), (6, 7), (2, 8)]

result_list = []

for i in tuple_list:
    mult = 1
    for num in i:
        mult *= num
    result_list.append(mult)

print(result_list)