user_input = input("Enter a list of numbers separated by commas: ")
user_list = user_input.split(",")

nested_list = []

for num in user_list:
    num = int(num.strip())
    if 4 <= len(str(num)) <= 6:
        sum_digits = 0
        mul_digits = 1
        for digit in str(num):
            sum_digits += int(digit)
            mul_digits *= int(digit)
        nested_list.append([num, sum_digits, mul_digits])

print("Data [number, sum of digits, product of digits]:", nested_list)
