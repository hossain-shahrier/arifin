"""
Write a python program that will take a list of numbers(integer) as an input from the user and does the following.

counts the number of valid, invalid, and duplicate numbers and prints these to the user.
stores the valid and invalid numbers in a list format and prints these to the user.
You need to make sure that a number is stored only Once.
Valid numbers: A number with a minimum length of 4 and a maximum length of 6 is considered to be valid for this assignment.
Calculate and print the percentage of valid numbers, invalid numbers, and duplicate numbers to the user.
==========================================================
Hints: Use membership operator in and not in for checking the duplicates.
For calculating the percentage, count the numbers of a particular number type.

"""
numbers_str = input("Enter a list of integers separated by spaces: ")
num = numbers_str.split(",")
valid_numbers = []
invalid_numbers = []
duplicate_numbers = []
numbers = []
for i in num:
    numbers.append(str(i.strip()))

for num in numbers:
    if len(num) >= 4 and len(num) <= 6 and num.isdigit():
        if num not in valid_numbers:
            valid_numbers.append(num)
        else:
            duplicate_numbers.append(num)
    else:
        if num not in invalid_numbers:
            invalid_numbers.append(num)

total_numbers = len(numbers)
valid_count = len(valid_numbers)
invalid_count = len(invalid_numbers)
duplicate_count = len(duplicate_numbers)

valid_percentage = (valid_count / total_numbers) * 100
invalid_percentage = (invalid_count / total_numbers) * 100
duplicate_percentage = (duplicate_count / total_numbers) * 100

print("Total numbers present in the given string:", total_numbers)
print("Valid number count:", valid_count)
print("Valid numbers in list:", valid_numbers)
print("Invalid number count:", invalid_count)
print("Invalid numbers in list:", invalid_numbers)
print("Duplicate number count:", duplicate_count)
print("Duplicate numbers in list:", duplicate_numbers)
print("Valid number percentage(%):", valid_percentage)
print("Invalid number percentage(%):", invalid_percentage)
print("Duplicate number percentage(%):", duplicate_percentage)
