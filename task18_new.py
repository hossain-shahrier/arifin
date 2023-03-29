list_1 = input()
list_2 = input()
new = []
comm = []
list_1 = list_1.split(", ")
list_2 = list_2.split(", ")
print(list_1)
print(list_2)


for i in list_1:
    new.append(i)
new_2 = []
for i in list_2:
    new_2.append(i)
for i in new:
    if i in new_2 and i not in comm:
        comm.append(i)
print(comm)
