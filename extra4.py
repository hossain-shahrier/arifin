""" Assume, you have been given a list T and a number, N. Now, create a list by concatenating the input list
which range goes from 1 to N.
Sample input1:
T = ['p', 'q']
N = 5
Sample Output1:
['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

"""
T = ['p', 'q', 'r','s']
N = 2
result = []
for n in range(1, N + 1):
    string = ""
    for t in T:
        result.append(t + str(n))

print(result)
