import random

def quizz():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    result = num1 + num2
 
    equal = int(input(f" What is {num1} + {num2}: "))
    if equal == result:
        print("You're right. :) Congrats")
    else:
        print(f"You're wrong the resutl is: {result}")

quizz()