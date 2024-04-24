# Writes a program that allows a user to simulate
# d-sided dice. Then print the total displayed numbers of each dice.
import random

number_of_dice = int(input('Number of dice to roll (any non-positive value to exit): '))
number_of_side = int(input('Number of sides per die (any non-positive value to exit): '))
total = 0
dice = 1
count = 0

print(f'\nRolling {number_of_dice}d{number_of_side}...')
while dice <= number_of_dice:
    display = random.randint(0, number_of_side)
    count = count + 1
    total = total + display
    print(f"Die {count}: {display}")
    dice = dice + 1
print(f"Total: {total}")

    


