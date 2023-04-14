tuple_of_tuples = eval(input("Enter a tuple of tuples: "))
# (33,21,11,30,45,56...)
# input_tuple = tuple(tuple(map(int, t.strip('()').split(','))) for t in input("Enter a tuple of tuples: ").split('),('))

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
