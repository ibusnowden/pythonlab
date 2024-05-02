import pet

name = input("Enter the pet name: ")
type = input("Enter the animal type: ")
age = int(input("Enter the animal age: "))
object = pet.Pet(name,  type, age)

new_name = object.get_name()
new_age = object.get_age()
new_type = object.get_animal_type()

print(f'\nName: {new_name}')
print(f'Type: {new_type}')
print(f'Age: {new_age}')