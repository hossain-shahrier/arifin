a_tuple = ([1, 2, 3], [4, 5, 6,4], [7, 8, 9], [10, 11, 12])
user_input = input("Enter a number:")
for i in a_tuple:
    i[-1] = user_input
print(a_tuple)