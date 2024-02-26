# Get three different integers from user
num1 = int(input("Please Enter First Number: "))
num2 = int(input("Please Enter Second Number: "))
num3 = int(input("Please Enter 3rd Number: "))

# Output sum of all the numbers
sum_all_numbers = num1 + num2 + num3
print(f"Sum of the all the numbers: {sum_all_numbers}")

# Subtract num1 from num2
subracted_num = num1 - num2

# Output the result
print(f"The first number minus the second number: {subracted_num}")

# Multiply num3 from num1
multiplied_num = num3 * num1

# Output the result
print(f"The third number multiplied by the first number: {multiplied_num}")

# Division the sum of all the numbers by third number
divided_num = sum_all_numbers/num3

# Output the result
print(f"The sum of all three numbers divided by the third number: {divided_num}")