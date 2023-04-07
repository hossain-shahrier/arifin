my_str = input("Enter a string: ")
my_dict = {

}

for char in my_str.lower():
    # python programming is fun
    # (a to z)
    if 'a' <= char <= 'z' or '0' <= char <= '9':
        my_dict[char] = my_dict.get(char, 0) + 1

print(my_dict)
