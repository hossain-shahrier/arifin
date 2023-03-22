number_list = []

for i in range(5):
    number = int(input("Enter your number: "))
    number_list.append(number)

# [1,2,3,4,5]
print("Reverse")
for i in range(len(number_list) - 1, -1, -1):
    print(number_list[i])

