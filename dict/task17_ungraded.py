my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue', 'a5': None}

new_dict = {}

for key, value in my_dictionary.items():
    if value is not None:
        new_dict[key] = value

# new_dict = {'c1': 'Red', 'c2': 'Green','d4': 'Blue'}
print(new_dict)
#
# my_dictionary2={
#
# }
# my_dictionary2['c1'] = 'Red'
