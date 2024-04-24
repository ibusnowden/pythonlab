males = int(input("number of males: "))
females = int(input("number of females: "))
total = (males + females)
m_p = males / total
f_p = females / total

print(f"The precentage of males is: {m_p:.0%}")
print(f"The precentage of females is: {f_p:.0%}")