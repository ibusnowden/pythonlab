start_n_organisms = int(input("Starting number of organisms: "))
average_d_increase = float(input("Average daily increase(%): "))
n_days = int(input("Number of days to multiply: "))

percentage = (average_d_increase / 100) 
print("Day\t\tAproximate Population")
for n in range(n_days):
    print(f"{n+1}\t\t{start_n_organisms}")
    start_n_organisms = start_n_organisms+ start_n_organisms * percentage
    
