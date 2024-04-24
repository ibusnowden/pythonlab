
# Writes a program that print 
# from a simple calculator

#calculator function 
def calculator(operation, num1, num2):
    if operation == 'add':
         return num1 + num2
    elif operation == 'multiply':
         return num1 * num2
    elif operation == 'substract':
         return num1 - num2
    elif operation == 'divide':
         return num1 / num2

#main function
def main():
    calcul = input("Enter the operation: ")
    number1 = int(input("Enter a number1: "))
    number2 = int(input("Enter number2: "))
    result = calculator(calcul, number1, number2)
    if number2 == 0 and calcul == 'divide':
        print("division by zero is not allowed")
    else:
        print(result)

main()

    

