import employee

employer1 = employee.Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employer2 = employee.Employee("Mark Jones", 39119, "IT      ", "Programmer")
employer3 = employee.Employee("Joy Rogers", 81774, "Manufacturing", "Engineeer")

print(f"{'Name':<12}\t{'ID Number':<12}\t{'Department':<12}\t{'Job Title':<12}")
print(f"{'-' * 60}")
print(employer1)
print(employer2)
print(employer3)