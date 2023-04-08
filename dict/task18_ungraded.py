# Given dictionary
dict_1 = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}

# lower_upper = input("Enter lower and upper range (inclusive and exclusive) separated by a comma: ")
# lower = int(lower_upper.strip().split(",")[0])
# upper = int(lower_upper.strip().split(",")[1])

lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

output = {}

for key, value in dict_1.items():
    if lower <= value < upper:
        output[key] = value

# Printing the extracted dictionary items
print(output)
