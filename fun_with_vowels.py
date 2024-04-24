# Count vowels
def count_vowels(string):
    count_vowel = 0
    vowels = ['a', 'A', 'i', 'I', 'o', 'O', 'e', 'E', 'u', 'U']
    for x in range(len(string)):
        if string[x] in vowels:
            count_vowel += 1
    print(f"{count_vowel}")

# Count Syllabes
def count_syllabes(string1):
    count_syllab = 0
    vowels = ['a', 'A', 'i', 'I', 'o', 'O', 'e', 'E', 'u', 'U']

    for i in range(len(string1)):
        if string1[x] in vowels:
            count_syllab += 1
        break

    for x in range(1, len(string1)):
        if string1[x] in vowels:
            count_syllab += 1
    print(count_syllab)

# Test
def main():
    count_vowels("")
    count_vowels("Z")
    count_vowels("sloth")
    count_vowels("SLOTh")
    count_vowels("slothy")
    count_vowels("ABACUS")

    print()
    
    count_syllabes("")
    count_vowels("Z")
    count_vowels("i")
    count_vowels("OWL")
    count_vowels("tomato")
    count_vowels("write")
    

main()


    
        

