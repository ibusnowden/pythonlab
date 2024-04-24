# This program displays the factorial of a number.
num = int(input("Enter a integer: "))
result = 1
counter = 0
change = num

while counter < num:
    result *= change
    change -= 1
    counter += 1
print(f"{num}! is {result}")