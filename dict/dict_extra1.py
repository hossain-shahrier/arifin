dict1 = {'w': 50, 'y': 'Green', 'a': 300, 'z': 400}
dict2 = {'y': 'Red', 'a': 200, 'b': 4, 'z': 600}

new_dict = {

}
for key in dict1:
    if key in dict2:
        new_dict[key] = [dict1[key], dict2[key]]
    #     new_dict['y'] = ['Green','Red']
    else:
        new_dict[key] = [dict1[key]]
#         new_dict['w'] = [dict1['w']]

for key in dict2:
    if key not in new_dict:
        new_dict[key] = [dict2[key]]

print(new_dict)
