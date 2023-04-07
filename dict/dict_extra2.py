dict_1 = {"a": [5, 2, 55, 17], "P": (11, 121, 222), "B": (37, 53, 71), "c": [45, 92, 50]}

dict_primes = {}

for key, value in dict_1.items():
    if key.islower():
        prime_numbers = []
        for num in value:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_numbers.append(num)
        dict_primes[key] = prime_numbers
    # if the key is in uppercase, check for prime numbers in the tuple
    elif key.isupper():
        prime_numbers = ()
        for num in value:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_numbers += (num,)
        dict_primes[key] = prime_numbers

# print the final dictionary
print(dict_primes)
