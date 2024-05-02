temperature = float(input("Enter the current temperature in Celsius: "))

if temperature <= 0:
    weather_condition = "freezing"
    print(f"The weather conditions are {weather_condition}.")
elif temperature > 0 and temperature <= 10:
    weather_condition = "cold"
    print(f"The weather conditions are {weather_condition}.")
elif temperature > 10 and temperature <= 20:
    weather_condition = "cool"
    print(f"The weather conditions are {weather_condition}.")
elif temperature > 20 and temperature <= 30:
    weather_condition = "warm"
    print(f"The weather conditions are {weather_condition}.")
elif temperature > 30:
    weather_condition = "hot" 
    print(f"The weather conditions are {weather_condition}.")