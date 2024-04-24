number = int(input("Please enter a number in the range 10 to 40:"))

while number < 10 or number > 40:
    print('Sorry the number must be betweeen 10 and 40. Please try again.')
    number = int(input("Please enter a number in the range 10 to 40:"))

print(f"You entered {number}.This is a valid number")