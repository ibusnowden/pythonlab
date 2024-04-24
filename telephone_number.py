string = input("Enter your 10 character telephone number in the form (XXX-XXXX-XXX) : ")
display = []
for char in string:
    if char.isnumeric() or char == '-':
        display.append(char)
    elif char == 'A' or char == 'B' or char == 'C':
        display.append('2')
    elif char == 'D' or char == 'E' or char == 'F':
        display.append('3')
    elif char == 'G' or char == 'H' or char == 'I':
        display.append('4')
    elif char == 'J' or char == 'J' or char == 'L':
        display.append('5') 
    elif char == 'M' or char == 'N' or char == 'O':
        display.append('6')
    elif char == 'P' or char == 'Q' or char == 'R':
        display.append('7')
    elif char == 'T' or char == 'U' or char == 'V':
        display.append('8')
    elif char == 'W' or char == 'X' or char == 'Y':
        display.append('p')
print(''.join(display))