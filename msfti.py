a = [1, 4, 5, 6, 9, 9]
b = [4, 4, 8, 9, 9,]
c = a + b
c.sort()
f = c.count(4)
n = c.count(9)

print(f"4:{f} ", end='')
print(f"9:{n}")