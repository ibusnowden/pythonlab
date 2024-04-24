
# Compound the retirement
current_age = int(input("Current age: "))
initial_deposit = int(input("Starting balance: "))
retirement_age = int(input("Target retirement age: "))
target_balance = int(input("Target balance at retirement: "))
annual_contribution = int(input("Annual contribution: "))
interest_rate = int(input("Project annual growth (percent): "))

start = initial_deposit
print("Projected growth")  
print("Age\t\tYear Start\t\tGrowth\t\tExtra\t\tYear End")
while current_age < retirement_age:
    #interest
    interest = start * interest_rate / 100
    end = start + interest + annual_contribution
    growth = end - (annual_contribution + start)
    if current_age > 25:
        annual_contribution = 0
    print(f"{current_age}\t\t${start:.2f}\t\t${growth:.2f}\t\t${annual_contribution:.2f}\t\t${end:.2f}")

    start = end
    current_age = current_age + 1 