username = 'johndoe'
password = 'secret1234'

user = input("Please enter your username: ")
pass_w = input("Please enter your password: ")

while user != username or pass_w != password:
    print("Sorry, your username or password is incorrect.Please try again.")   
    user = input("Please enter your username: ")
    pass_w = input("Please enter your password: ")

print("You entered the system succesfully.")

