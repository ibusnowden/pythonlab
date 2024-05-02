LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    birthdays = {}

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == delete:
            delete(birthdays)

def get_menu_choice():
    print()
    print("Friends and their Birthdays")
    print("-----------------------------")
    print("1. Look up a birthday")
    print("2. Add a new birthday")
    print("3. Change a birthday")
    print("4. Delete a birthday")
    print("5. Quit the program")

    choice = int(input('Enter your choice: '))

    while choice < look_up or choice > QUIT:
        choice = int(input("Enter a valid choice: "))
    return choice

def look_up(birthdays):
   name = input("Enter a name: ")
   print(birthdays.get(name, "Not found."))

def add(birthdays):
   