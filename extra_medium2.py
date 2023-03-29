"""Write a python program that will take a number a list of numbers(integer) as an input from the user
and print whether the number is Awesome or not."""
user_list = []
size = int(input("Enter list size: "))

for i in range(size):
    inputs = int(input("Enter number: "))
    user_list.append(inputs)

for num in user_list:
    num_str = str(num)
    is_awesome = True
    for i in range(1, len(num_str)):
        if int(num_str[i]) >= int(num_str[i-1]):
            is_awesome = False
            break
    if is_awesome and len(num_str) > 1:
        print(num, "is an awesome number.")
    else:
        print(num, "is a not-so-awesome number.")