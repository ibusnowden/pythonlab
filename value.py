def main():
    value = float(input("Enter account's present value: "))
    rate = float(input("Enter interest rate: "))
    months = float(input("Enter number of months: "))
    future = earning(value, rate, months)
    print(f"future value is: ${future:.2f}")

def earning(p_value, interest_rate, n_months):
    future_value = p_value * (1 + interest_rate)**n_months
    return future_value

main()