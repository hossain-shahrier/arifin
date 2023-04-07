tuple_of_tuples = eval(input("Enter a tuple of tuples: "))

averages = []
for i in tuple_of_tuples:
    avg = sum(i) / len(i)
    averages.append(avg)

print("Average of tuples:", averages)

max_sum = 0
max_tuple = ()
for i in tuple_of_tuples:
    tup_sum = sum(i)
    if tup_sum > max_sum:
        max_sum = tup_sum
        max_tuple = i

print("Tuple with maximum sum is", max_tuple)
