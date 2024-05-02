"""
Value returned functions:
A value returning function is a function that returns value back to the program that called it.
Standard Library Function: int(), float(), input()
Modules: files that stores functions of the STL
"""
import random
"""
MIN = 1
MAX = 6

def main():
    again = 'y'

    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print("Their values are:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        again = input('Roll them again? (y = yes): ')
main()

HEADS = 1
TAILS = 2
TOSSES = 10

def test():
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('HEADS')
        else:
            print('TAILS')
            
test()

def f():
    first_age = int(input('Enter your age: '))
    second_age = int(input("Enter your sister's age: "))

    total = total_age(first_age, second_age)
    print(f'Together your are {total} years old.')

def total_age(age1, age2):
    result = age1 + age2
    return result

f()

DISCOUNT_P = 0.20

def ff():
    reg_price = get_reg_price()
    sale_price = reg_price - discount(reg_price)
    print(f'The sale price is ${sale_price:,.2f}')

def get_reg_price():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    result = price * DISCOUNT_P
    return result

ff()
"""
