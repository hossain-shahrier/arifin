number_list = []
new_list = []

loop_time = int(input("How much inputs you want to take: "))
for i in range(loop_time):
    number = int(input("Enter a number: "))
    number_list.append(number)

if len(number_list) < 4:
    print("Not possible")
else:
    new_list = number_list[2:-2]

print(new_list)
