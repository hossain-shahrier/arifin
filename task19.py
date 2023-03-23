list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

# create a new empty list to store unique elements
unique_elements = []

for element in list_one:
    if element not in unique_elements:
        unique_elements.append(element)

for element in list_two:
    if element not in unique_elements:
        unique_elements.append(element)

print("Output:", unique_elements)
