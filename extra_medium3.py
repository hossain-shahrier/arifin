"""
Write a python program that will take a string as input from the user where each number is separated by a comma.
Then gets the numbers from the given string and removes all extra spaces. Stores the clean numbers in a list and prints it.
==========================================================
Hints: For obtaining the numbers from the string, use split(). For cleaning the data, use strip().
==========================================================
Sample Input1:
"97821, 1 	, 97210,   963,    979210 , 979210 "
Sample Output1:
Data after cleaning: [97821, 1, 97210, 963, 979210, 979210]

"""
user_input = input("Enter your numbers,separated by comma:")

user_input = user_input.split(",")

clean_list = []
for i in user_input:
    clean_list.append(int(i.strip()))

print("Data after cleaning : ",clean_list)
