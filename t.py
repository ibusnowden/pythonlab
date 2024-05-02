nums = []
m = []
t = input().split()
for i in t:
  nums.append(int(i))

for x in nums:
   if x < 0:
     m.append(x)
   m.sort(reverse=True)
for b in m:
  print(b, end=' ')

"""
name1 = input()
name2 = input()

# Modify the following line
travel_str = (f"{name1} and {name2} are best friends,"
              f" but {name1} lives 40 miles north of {name2}."
              f" {name1} wants to visit {name2} next summer.")

# format() replaces the curly braces in a string with variables.
# This method is being used to test your code.
new_str = travel_str.format(name1, name2)
print(new_str)

###################
cities = {
    'Montreal': 982,
    'Toronto': 438,
    'Paris': 958,
    'Austin': 550,
    'Nairobi': 5259,
    'Chicago': 309,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)
"""