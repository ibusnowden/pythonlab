colors_available = input().split()
favorites_list = input().split()
  
print('Available colors:', end=' ')
for color in colors_available:
    print(color, end=' ')
print()

print('Favorite colors:', end=' ')
for color in favorites_list:
    print(color, end=' ')
print()

''' Your code goes here '''
for c in colors_available[:]:
    if c not in favorites_list:
        print(f'{c} not considered')
        colors_available.remove(c)

print('Remaining colors:', end=' ')
for color in colors_available:
    print(color, end=' ')
print()
