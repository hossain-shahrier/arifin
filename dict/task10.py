my_dict = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}


max_value = -1
max_key = None

for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print("The highest selling book genre is '{0}' and the number of books sold are {1}.".format(max_key, max_value))
