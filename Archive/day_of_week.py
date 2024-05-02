
import math

m = int(input("Enter the month (1-12): "))
q = int(input("Enter the day of the month (1-31): "))
year = int(input("Enter the year: ")) - 1

K = 99
J = 19

h =  (q + (13 * (m + 1) / 5 ) + K + (K / 4) + (J/ 4) + (5 * J)) % 7

h = math.floor(h)

if h == 0: 
    day = "Saturday"  
    print(f"{m}/{q}/{year} is {day}")
elif h == 1: 
    day = "Sunday"  
    print(f"{m}/{q}/{year} is {day}")
elif h == 2:
    day = "Monday"
    print(f"{m}/{q}/{year} is {day}")
elif h == 3:
    day = "Tuesday"
    print(f"{m}/{q}/{year} is {day}")
elif h == 4:
    day = "Wednesday"
    print(f"{m}/{q}/{year} is {day}")
elif h == 5:
    day = "Thursday"
    print(f"{m}/{q}/{year} is {day}")
elif h == 6:
    day = "Friday"
    print(f"{m}/{q}/{year} is {day}")
