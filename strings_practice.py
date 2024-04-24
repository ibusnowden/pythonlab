# slicing string using a loop
word = input("Enter a string: ")
for i in range(len(word)):
    print(i, word[i], word[0:i+1])