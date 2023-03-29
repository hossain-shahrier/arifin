List1 = [10, 20, 30, 40]
List2 = [100, 200, 300, 400]

modified_List2 = []
# Reverse List2
for i in range(len(List2) - 1, -1, -1):
    modified_List2.append(List2[i])

for i in range(len(List1)):
    print(List1[i], " ", modified_List2[i])
