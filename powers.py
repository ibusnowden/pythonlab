# This program display the power of an integer input
# By the n iterations of another integer.
num = int(input("Enter a integer: "))
power = int(input("Enter a power: "))
result = 1
count = 0

while count < power:
    count = count + 1
    result = result * num
print(f"{num} to the power of {power} is {result}.")