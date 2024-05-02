import random

print("Slotherius use Triple Claw Slah!")
charge = int(input("How many seconds would you like to charge? "))

damage1 = random.randint(15, 21)
damage2 = random.randint(15, 21)
damage3 = random.randint(23 - 10 * charge, 23 + 10 * charge)

print("\nDamage dealt:")
print("Attack1: ", damage1)
print("Attack2: ", damage2)
print("Attack3: ", damage3)