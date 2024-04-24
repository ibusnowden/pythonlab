# Review
# This program check the password
# If your input match the string your gain access
# If not you're blocked after 4th try.
password = input("Enter password: ")
attempt = 0
count = 3

while attempt < count:
    if password == 'sloth':
        print("Access granted.")
    else:
        print(f"incorrect password. You have {count} attempt(s) remaining.")
        count = count - 1
        input("Enter password: ")
print('Your account has been locked for 24 hours.')   

