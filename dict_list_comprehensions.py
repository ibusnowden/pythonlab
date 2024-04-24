# write a text that returns a list of dictionnay
number = int(input("Enter a number: "))

result = [dict({number+1 : {f"item {number+1}" : [(number+1)**(number+1)]*3}}) for number in range(number)]
print(result)
