import car1

my_car = car1.Car("Pontiac", 2022)

for a in range(0, 5):
    b = my_car.accelerate()
    speed = my_car.get_speed()
    print(f"acceleration {a}: {speed}")

print()

for x in range(0, 5):
    ac = my_car.brake()
    speed = my_car.get_speed()
    print(f"brake {x}: {speed}")
