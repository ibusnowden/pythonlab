def f(number):
    return number**2

print("numbers\tsquares")
for i in range(10):
    print(f"{i} \t{f(i)}")