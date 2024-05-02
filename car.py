# Cretaes a class named Car
# With a constructor and attributes
class Car:
    def __init__(self, __make, __model, __color, __price):
        self.__make = __make
        self.__model = __model
        self.__color = __color
        self.__price = __price
        self.__mileage = 0

    def set_price(self, p):        # Set the price
        self.__price = p

    def paint(self, c):            # Set the color
        self.__color = c
    
    def show_car_info(self):       # Car info
        return f'{self.__make} {self.__model} {self.__color} {self.__price} {self.__mileage}'
    
    def travel(self, distance):    # Distance travelled
        self.__mileage += distance

# Creates two objects
new_car1 = Car('Porsche', '718 Cayman GTS 4.0', 'black', '$95000')
new_car2 = Car('Toyota', 'Corolla LE', 'red', '$22,050')

# Test and method calling
#print(new_car1.show_car_info())
#print(new_car2.show_car_info())

# Paint both car witha a new color
new_car1.paint('Gray')
new_car2.paint('Blue')

# price change
new_car1.set_price('$86,000')
new_car2.set_price('$19,500')

# Distance travelled
new_car1.travel(2500)
new_car2.travel(4000)

# Test Output
print(new_car1.show_car_info())
print(new_car2.show_car_info())