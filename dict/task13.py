list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

dict_1 = {}

for key, value in list_1:
    if key in dict_1:
        dict_1[key].append(value)
    else:
        dict_1[key] = [value]

print(dict_1)
