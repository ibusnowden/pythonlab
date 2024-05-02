# This program display the favorite animal
# and the most popular of them. Each animal might be 
# stored in the list multiple time.

# attributes.
animal_list = []
owl_count = 0
sloth_count = 0
dinosaur_count = 0
cat_count = 0
platypus_count = 0

# The program exit if we input x in case insensitive.
for x in range(1, 16):
    animal = input(f'Enter favorite animal from survey #{x}: (X to exit) ') 
    if animal == 'X' or animal == 'x':
      break
    animal_list.append(animal)
print()

# Count the number of appearance of each animal.
for x in animal_list:
  if x.lower() == 'owl':
    owl_count += 1 
  elif x.lower() == 'sloth':
    sloth_count += 1 
  elif x.lower() == 'dinosaur':
    dinosaur_count += 1
  elif x.lower() == 'cat':
    cat_count += 1
  elif x.lower() == 'platypus':
    platypus_count += 1

# Output.
print('Summary of responses:')
print(f'owl - {owl_count}')
print(f'sloth - {sloth_count}')
print(f'dinausor - {dinosaur_count}')
print(f'cat - {cat_count}')
print(f'platypus - {platypus_count}\n')

print('Most popular animals')
if owl_count >= 4:
  print("owl")
if sloth_count >= 4:
  print('sloth')
if dinosaur_count >= 4:
  print('dinausor')
if cat_count >= 4:
  print('cat')
if platypus_count >= 4:
  print('platypus')

