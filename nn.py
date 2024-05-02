
password = input("Enter password: ")
attempt = 0
count = 3

while attempt < count:
    
    if password == "lock":
        print("Access granted.")
        exit()
    else:
        print(f"incorrect password. You have {count} attempt(s) remaining.")
        input("Enter password: ")
        count = count - 1
print('Your account has been locked for 24 hours.')   

        

