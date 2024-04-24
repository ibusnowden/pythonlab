num = int(input("Enter an integer (enter 0 to exit: "))
count = 0

while num != 0:
    num = int(input("Enter an integer (enter 0 to exit: "))
    if num >= 0:
     count += 1
print(f"The count of positive integers entered is {count}.")