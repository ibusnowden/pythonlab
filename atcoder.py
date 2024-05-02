"""
a = int(input())
b, c  = map(int, input().split())
st = input()

s = a + b + c
print(f"{s} {st}")

############

input_data = input()
pairs = input_data.split()
contact_list = {}
for pair in pairs:
    name, phone_number = pair.split(',')
    contact_list[name] = phone_number
###############
from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car

print(chevy_blazer)
print(chevy_impala)
"""
''' Type your code here. '''
nums = []
it = input().split()
a, b = map(int, input().split())
for x in it:
   nums.append(int(x))
#nums = [int(w) for w in it] another way of adding elements
while a < b:
  for al in nums:
    if al >= a and al < b:
        print(al, end=',')
  break



