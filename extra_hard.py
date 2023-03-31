# Part 1: Get the numbers from the given string, remove all extra spaces.
input_string = input("Enter a string of numbers separated by commas: ")
clean_data = [int(num.strip()) for num in input_string.split(",")]

# Print the clean data to the user.
print("Data after cleaning:", clean_data)

# Part 2: Count the number of valid, invalid, and duplicate numbers.
valid_nums = []
invalid_nums = []
duplicates = []
for num in clean_data:
    # Check if number is valid.
    if 4 <= len(str(num)) <= 6:
        if num not in valid_nums:
            valid_nums.append(num)
        else:
            duplicates.append(num)
    else:
        if num not in invalid_nums:
            invalid_nums.append(num)

# Print the counts to the user.
total_count = len(clean_data)
valid_count = len(valid_nums)
invalid_count = len(invalid_nums)
duplicate_count = len(duplicates)
print("Total numbers present in the given string:", total_count)
print("Valid number count:", valid_count)
print("Invalid number count:", invalid_count)
print("Duplicate number count:", duplicate_count)

# Part 3: Store the valid and invalid numbers in a list format.
valid_list = valid_nums
invalid_list = invalid_nums

# Print the valid and invalid numbers to the user.
print("Valid numbers in list:", valid_list)
print("Invalid numbers in list:", invalid_list)

# Part 4: Calculate and print the percentage of valid, invalid, and duplicate numbers.
valid_percentage = valid_count / total_count * 100
invalid_percentage = invalid_count / total_count * 100
duplicate_percentage = duplicate_count / total_count * 100
print("Valid number percentage(%):", valid_percentage)
print("Invalid number percentage(%):", invalid_percentage)
print("Duplicate number percentage(%):", duplicate_percentage)

# Part 5: Store the valid numbers, the sum of digits, and multiplication of the digits for each valid number.
valid_data = []
for num in valid_list:
    digits = [int(digit) for digit in str(num)]
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    valid_data.append([num, digit_sum, digit_product])

# Print the nested list to the user.
print("Data of valid numbers:\n[number, sum of digits, product of digits]:")
print(valid_data)

# Part 6: Check whether the valid numbers are Awesome or not.
print("^^ Awesomeness checking of the Valid numbers ^^")
for num_data in valid_data:
    num = num_data[0]
    digits = [int(digit) for digit in str(num)]
    is_awesome = True
    for i in range(1, len(digits)):
        if digits[i] >= digits[i-1]:
            is_awesome = False
            break
    if is_awesome:
        print(num, "is an awesome number.")
    else:
        print(num, "is a not-so-awesome number.")
