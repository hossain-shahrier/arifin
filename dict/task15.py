tuple_list = [(11, 22), (33, 55), (55, 77), (11, 44)]

result_list = []

for tup in tuple_list:
    mult = 1
    for num in tup:
        mult *= num
    result_list.append(mult)

print(result_list)