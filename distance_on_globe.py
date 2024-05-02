import math

RADIUS = 3958.8
print("Enter lat/long of starting point (in degrees): ")

lat_1 = float(input("Lat: "))
long_1 = float(input("Long: "))

print("\nEnter lat/long of ending point (in degrees): ")
lat_2 = float(input("Lat: "))
long_2 = float(input("Long: "))

p1_lat = (lat_1 * math.pi) / 180
p2_lat = (lat_2 * math.pi) / 180
p1_long = (long_1 * math.pi) / 180
p2_long = (long_2 * math.pi) / 180 

A = (math.sin((p2_lat - p1_lat) / 2))**2 + math.cos(p1_lat) * math.cos(p2_lat) * (math.sin(p2_long - p1_long) / 2)**2
distance = 2 * RADIUS * math.atan2(math.sqrt(A), math.sqrt(1 - A))

print(f"\nDistance is: {distance:.1f} mi.")