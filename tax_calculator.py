
income = int(input("What was you 2023 income? "))

if income <= 11000:
    tax = income * 0.1
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {(11000 * 0.1):.2f}")
    print(f"Total tax owed:\t\t\t$ {tax:.2f}")
    print(f"Effective tax rate: \t\t{rate:.1f}%")
elif income > 11000 and income <= 44725:
    tax = 11000 * 0.1 + (income - 11000) * 0.12
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {(11000 * 0.1):.2f}")
    print(f"$ {11000} - $ {44725}:\t\t$ {(4047):.2f}")
    print(f"Total tax owed:\t\t\t$ {tax:.2f}")
    print(f"Effective tax rate: \t\t{rate:.1f}%")
elif income > 44725 and income <= 95375:
    tax = (11000 * 0.1) + (44725 * 0.12) + (income - 44725) * 0.22
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {1100:.2f}")
    print(f"$ {11000} - $ {44725}:\t\t$ {4047:.2f}")
    print(f"$ {44725} - $ {95375}:\t\t$ {6078:.2f}")
    print(f"Total tax owed:\t\t\t$ {tax:.2f}")
    print(f"Effective tax rate: \t\t{rate:.1f}%")
elif income > 95375 and income <= 182100:
    tax = (11000 * 0.1) + (44725 * 0.12) + (95375 * 0.22) + (income - 95375) * 0.24
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {1100:.2f}")
    print(f"$ {11000} - $ {44725}:\t\t$ {4047:.2f}")
    print(f"$ {44725} - $ {95375}:\t\t$ {6078:.2f}")
    print(f"$ {95375} - $ {182100}:\t\t$ {20814:.2f}")
    print(f"Total tax owed:\t\t\t$ {tax:.2f}")
    print(f"Effective tax rate: \t\t{rate:.1f}%")
elif income > 182100 and income <= 231250:
    tax = (11000 * 0.1) + (44725 * 0.12) + (95375 * 0.22) + (182100 * 0.24) + (income - 182100) * 0.32
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {1100:.2f}")
    print(f"$ {11000} - $ {44725}:\t\t$ {4047:.2f}")
    print(f"$ {44725} - $ {95375}:\t\t$ {6078:.2f}")
    print(f"$ {95375} - $ {182100}:\t\t$ {20814:.2f}")
    print(f"$ {182100} - $ {231250}:\t\t$ {15728:.2f}")
    print(f"Total tax owed:\t\t\t$ {tax:.2f}")
    print(f"Effective tax rate: \t\t{rate:.1f}%")
elif income > 231250 and income <= 578125:
    tax = (11000 * 0.1) + (44725 * 0.12) + (95375 * 0.22) + (182100 * 0.24) + (231250 * 0.32) + (income - 231250) * 0.35
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {1100:.2f}")
    print(f"$ {11000} - $ {44725}:\t\t$ {4047:.2f}")
    print(f"$ {44725} - $ {95375}:\t\t$ {6078:.2f}")
    print(f"$ {95375} - $ {182100}:\t\t$ {20814:.2f}")
    print(f"$ {182100} - $ {231250}:\t\t$ {15728:.2f}")
    print(f"$ {231250} - $ {578125}:\t\t$ {tax:.2f}")
else:
    tax = (11000 * 0.1) + (44725 * 0.12) + (95375 * 0.22) + (182100 * 0.24) + (231250 * 0.32) + (231250 * 0.35) + (income - 578125) * 0.37
    rate = (tax * 100) / income
    print(f"    First $ {11000}:\t\t$ {1100:.2f}")
    print(f"$ {11000} - $ {44725}:\t\t$ {4047:.2f}")
    print(f"$ {44725} - $ {95375}:\t\t$ {6078:.2f}")
    print(f"$ {95375} - $ {182100}:\t\t$ {20814:.2f}")
    print(f"$ {182100} - $ {231250}:\t\t$ {15728:.2f}")
    print(f"$ {231250} - $ {578125}:\t\t$ {121406:.2f}")
    print(f"$ over {578125}:\t\t$ {213906:.2f}")
    print(f"Total tax owed:\t\t\t$ {tax:.2f}")
    print(f"Effective tax rate: \t\t{rate:.1f}%")
