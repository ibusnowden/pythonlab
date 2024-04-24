x_value = int(input("Enter value for x: "))
y_value = int(input("Enter value for y: "))

print(f"\nBefore swap: x = {x_value}, y = {y_value}")

temp = x_value
x_value = y_value
y_value = temp

print(f"After swap: x = {x_value}, y = {y_value}")