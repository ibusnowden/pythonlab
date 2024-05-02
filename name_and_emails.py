## The code is not working 

def data():
    with open("name_and_emails.txt", "r") as fd:
        new_data = {}
        for line in fd:
            name, email = line.strip().split(":")
            new_data[name] = email
        return new_data
        
def s_data(new_data):
    with open("name_and_emails.txt", "w") as fd:
        for name, email in new_data.items:
            fd.write(f"{name} : {email}\n")

def get_menu_choice():
    print()
    print("-----------------------------")
    print("1. Look up a email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete an existing email address")
    print("5. Quit the program")

def lookup(new_data):
    name = input("Enter a name: ")
    if name in new_data:
        print(f"Email address: {new_data[name]}")
    else:
        print("Name not found")

def add(new_data):
    name = input("Enter name: ")
    email = input("Enter email address: ")
    new_data[name] = email
    print('Name and email address added')

def change(new_data):
    name = input("Enter name: ")
    if name in new_data:
        email = input('Enter new email address: ')
        new_data[name] = email
        print('Email address updated')
    else:
        print("Name not found.")

def delete(new_data):
    name = input("Enter a name: ")
    if name in new_data: 
        del new_data[name]
        print("Name and email address deleted.")
    else:
        print("Name not found.")

def main():
    new_data = data()
    while True:
       get_menu_choice()
       choice = input("Enter your choice: ")
       if choice == "1":
           lookup(new_data) 
       elif choice == "2":
           add(new_data)
       elif choice == "3":
           change(new_data)
       elif choice == "4":
           delete(new_data)
       elif choice == "5":
           s_data(new_data)
           print("Saved")
           break
       else:
           print("Invalid choice")
main()