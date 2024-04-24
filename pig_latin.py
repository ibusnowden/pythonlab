word = input('Enter a string: ')
letter = word.split()
for char in letter:
    print(char[1:] + char[0] + "AY", end = " ")
print()