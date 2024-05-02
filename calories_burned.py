CALORIES = 4.2
minutes = 5

while minutes <= 60:
    calories_b = minutes * (CALORIES / 5)
    print(f'Calories burned after {minutes} minutes is {calories_b:.1f}')

    minutes = minutes + 5