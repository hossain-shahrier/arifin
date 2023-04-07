# Given list of tuples
list_of_tuples = [(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]

# Creating an empty dictionary
output_dict = {}

for i in list_of_tuples:
    # (20,'Sad')
    if i[1] in output_dict:
        output_dict[i[1]].append(i)
        # output_dict['Sad'] = [(20,'Sad'),(31,'Sad')]
    else:
        output_dict[i[1]] = [i]
#       output_dict[key] = [tuple]
#       output_dict['Sad']  = [(20,'Sad')]
print(output_dict)
