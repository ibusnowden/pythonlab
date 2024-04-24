word = input("Enter a sentence: ")
ch = word.split()
for x in ch:
    print(word[0].upper(), end = '')
    print(word[1:], end = '')
print()