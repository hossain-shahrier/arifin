my_list = ["hey", "there", "", "what's", "", "up", "", "?"]

new_list = []

for i in my_list:
    if i != "":
        new_list.append(i)

print(new_list)
