string = input('Enter a sentence: ')
strings = string.upper()
counter = 0
total_counter = 0
most_frequent_character = ""

for ch in strings:
        for str in strings:
            if str == ch:
                counter += 1
        if counter > total_counter:
            total_counter = counter
            most_frequent_character = ch
        counter = 0

print(f"The most frequent character is: '{most_frequent_character}'")


    