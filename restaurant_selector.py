vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten_free = input('Is anyone in your party a gluten_free? ')

if (vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes'):
    print('Here are your restaurant choices: ')
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print('The Chef\'s Kitchen')
else:
    if (vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes'):
         print('Here are your restaurant choices: ')
         print('The Chef\'s Kitchen')
         print('Corner Cafe')