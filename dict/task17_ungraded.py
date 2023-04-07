my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue', 'a5': None}

new_dict = {}

for key, value in my_dictionary.items():
    if value is not None:
        new_dict[key] = value

print(new_dict)
