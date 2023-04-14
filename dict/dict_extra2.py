dict_1 = {"N":(4,9,3),"k":[95,37,197],"F":(32,5,97),"s":[31,94,55]}
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

print(dict_primes)
