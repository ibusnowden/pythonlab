# Using list
def count_plurals(word_list):
    count = 0
    for x in range(len(word_list)):
        if word_list[x].endswith("s"):
            count = count + 1
            print(word_list[x], " yes")
        else:
            print(word_list[x], "no")
    print(count)

# Definition of my list
my_list = ['llama', 'status', 'gaps', 'mistral', 'oculus', 'ectas']
x_list = ['sloth', 'owls', 'sloths', 'bear', 'playthus']


count_plurals(x_list)
print()
count_plurals(my_list)