# This program defines sloth studying by displaying
# the number of sloth sight in a day

# This function counts the number of days
def count_treshold(data, n):
    number_of_days = 0
    for sloth_data in data:
        if sloth_data >= n:
            number_of_days += 1
    return number_of_days

# This function displays the average of sloth sighted each day
def average_treshold(data, n):
    number_of_days = 0
    sum = 0
    average = None
    for sloth_data in data:
        if sloth_data >= n:
            number_of_days += 1
            sum += sloth_data 
        average = sum / number_of_days
    return average

# Test function
def main():
    list_data = []
    days = int(input("How many days of data do you have? "))
    while days < 1:
        days = int(input("Must enter at least one day data! Try again: "))
        if days >= 1:
            days = days
    print()
    
    for x in range(1, days+1):
        d = int(input(f'Enter number of sloths sighted on day {x}: '))
        while d <= 0:
            d = int(input('Cannot be a negative number! Try again: '))
            if d > 0:
                d = d
        list_data.append(d)
    
    print()
    
    tresh_hold = int(input('Data collection complete. Enter a minimum treshold to analyze: '))
    print(f'\nNumber of days when at least {tresh_hold} sloths were sighted was: {count_treshold(list_data, tresh_hold)}')
    print(f'Average sloth sightings on those days is: {average_treshold(list_data, tresh_hold)}')
    
main()

    
