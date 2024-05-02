def main():
    fat_grams = int(input("Enter number of fat grams: "))
    carb_grams = int(input("Enter number of carb grams: "))
    calories_f_fat = fat_grams * 9
    calories_f_carb = carb_grams * 4
    print(f"Calories from fat is: {calories_f_fat}")
    print(f"Calories from carb is: {calories_f_carb}")
 
main()

