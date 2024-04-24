# Game of sloth
import random

count = 0
game = 1

print("Welcome to TWENTY SLOTHS, good luck!\n")
while game == 1:
    count = count + 1
    print(f"GAME {count}")
    print("------")
    bet_amount = int(input("\nEnter amount to bet: "))
    current_sloth = 1

    while bet_amount < 10:
      bet_amount = int(input("Bet must be at least $10, try again: "))
    print(f"\nCurrent sloths: {current_sloth}")
    print("1. Get 1-8 more sloths")
    print("2. Get 4-7 more sloths")
    print("3. Hold")

    choice = int(input("Enter your choice (1, 2, or 3): "))
    while choice > 3:
      print("Invalid choice. Let's try again..")
      print(f"\nCurrent sloths: {current_sloth}")
      print("1. Get 1-8 more sloths")
      print("2. Get 4-7 more sloths")
      print("3. Hold")
      choice = int(input("\nEnter your choice (1, 2, or 3): ")) 

    while choice == 1 or choice == 2:
        if choice == 1:
            x_1 = random.randint(1, 8)
            print(f"\nAdding {x_1}...")
            current_sloth += x_1
            print(f"\nCurrent sloths: {current_sloth}") 
            print("1. Get 1-8 more sloths")
            print("2. Get 4-7 more sloths")
            print("3. Hold")
       
        elif choice == 2:
            x_2 = random.randint(4, 7)
            current_sloth += x_2
            print(f"Adding {x_2}...")
            print(f"\nCurrent sloths: {current_sloth}") 
            print("1. Get 1-8 more sloths")
            print("2. Get 4-7 more sloths")
            print("3. Hold")
        choice = int(input("\nEnter your choice (1, 2, or 3): "))  

        if choice == 3 or current_sloth >= 21:
          print(f"Oh no, you're at {current_sloth}!")
    if current_sloth <= 14:
           print("You lose all the bet")
    elif current_sloth == 15:
           win = bet_amount * 0.25
           print(f"you won ${win:.2f}")
    elif current_sloth == 16:
           win = bet_amount * 0.5
           print(f"you won ${win:.2f}")
    elif current_sloth == 17:
           win = bet_amount * 1
           print(f"you won ${win:.2f}, Break even!")
    elif current_sloth == 18:
           win = bet_amount * 1.25
           print(f"you won ${win:.2f}")
    elif current_sloth == 19:
           win = bet_amount * 1.5
           print(f"you won ${win:.2f}")
    elif current_sloth == 20:
           win = bet_amount * 2
           print(f"you won ${win:.2f} Amazing, you gained money!")
    
    print(f"\nTotal game played: {count}")
    print(f"Net gain\loss: ${win:.2f}")

    game = int(input("\nEnter 1 to play anything else to exit: "))
print("Thanks for playing! Hope you come out ahead...")
 

""" 
count = 0
game = 1

while game == 1:
 count = count + 1
 print(f"GAME {count}")
 print("------")
 game = int(input("Enter 1 to play anything else to exit: "))

"""