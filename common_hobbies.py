
# This program find the common hobbies
# with a potential dating app match

# This function search if there is
# a common hobby which are string element stored in two different list
def find_common_hobbies(h1, h2):
    hobby = []
    for x in h1:
        for y in h2:
            if x.lower() == y.lower():
                hobby.append(x.lower())
    print(hobby)

# Unit test
test1 = ['Hiking', 'Gaming', 'Drawing']
test2 = ['Pottery', 'Cycling', 'sleeping']
test3 = ['Sloths', 'Guitars', 'Traveling']
test4 = ['TRAVELING', 'SLOTHS']
test5 = ['Watching Paint Dry', 'World Domination']
test6 = ['Painting', 'World Domination', 'Sloths']

# Function call
find_common_hobbies(test1, test2)
find_common_hobbies(test3, test4)
find_common_hobbies(test5, test6)