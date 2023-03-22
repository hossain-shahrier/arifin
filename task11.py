List_one = [1, 4, 3, 2, 6]
List_two = [5, 6, 9, 8, 7]

# Initialize flag to False
flag = False

# Loop through List_one and check if any element is present in List_two
for element in List_one:
    if element in List_two:
        flag = True
        break
if flag:
    print("True")
else:
    print("False")