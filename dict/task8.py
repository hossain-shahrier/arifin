input_dict = input("Enter a dictionary: ")

pairs = input_dict.split(",")
my_dict = {}

# key,value
for i in pairs:
    key, value = i.split(":")
    my_dict[key.strip()] = int(value.strip())

total = 0
count = 0

for value in my_dict.values():
    total += value
    count += 1

average = total / count

print("Average is:", average)
