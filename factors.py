# This program print all the factors of a number
# We compute the factor by using modulus operation
number = int(input("Enter a positive number: "))
print(f"Factors of {number}:")
result = 1

while result <= 40:
    if number % result == 0:
        print(result)
    result = result + 1