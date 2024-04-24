P = int(input("amount of money originally deposited: "))
n = int(input("The number of time per year: "))
t = int(input("number of years: "))
# The annual interest rate
r = float(input("the percentage: ")) / 100
A = P * (1 + r/n)**(n*t)

print(f"The money that will be in the account after {t} years is {A:.2f} $")
