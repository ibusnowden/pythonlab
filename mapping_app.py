# space between avenues and streets
INITIAL_BLOCK = 750
block1 =1
block2 = 1

# Input validation
def get_positive_integer_input(prompt):
    prompt = int(input(" "))
    while prompt < 0:
        prompt = int(input("Must enter a positive integer, try again: "))
        if prompt > 0:
            return prompt
    return prompt
    
# string ordinal number
def num_to_ordinal(n):
    
    if n == 1 or n == 21:
       return (f"{n}st")
    elif n == 2 or n == 22:
        return (f"{n}nd")
    elif n == 3 or n == 23:
        return (f"{n}rd")
    else:
        return (f"{n}th")

# print the directions
def get_directions(start_av, start_st, end_av, end_st):
    s_av = start_av
    s_st = start_st
    e_av = end_av
    e_st = end_st

    start_av = num_to_ordinal(start_av)
    start_st = num_to_ordinal(start_st)
    end_av = num_to_ordinal(end_av)
    end_st = num_to_ordinal(end_st)
    
    print(f"Directions from the {start_av} Ave. and {start_st} St. to {end_av} Ave. and {end_st} St.:")

    if s_av > e_av and e_st > s_st:
        block1 = INITIAL_BLOCK * (s_av - e_av)
        block2 = INITIAL_BLOCK * (e_st - s_st)
        print(f"Take {start_st} St. east for {block1} ft until you get to {end_av} Ave.")
        print(f"Turn left onto {end_av} Ave.") 
        print(f"Take {end_av} Ave. north for {block2} ft until you get to {end_st} St.")
        print("yay, you've arrived!")
    
    if s_av < e_av and e_st > s_st:
        block1 = INITIAL_BLOCK * (e_av - s_av)
        block2 = INITIAL_BLOCK * (e_st - s_st)
        print(f"Take {start_st} St. west for {block1} ft until you get to {end_av} Ave.")
        print(f"Turn rigth onto {end_av} Ave.")
        print(f"Take {end_av} Ave. north for {block2} ft until you get to {end_st} St.")
        print("yay, you've arrived!")

    if s_av == e_av and s_st > e_st:
        block1 = INITIAL_BLOCK * (s_st - e_st)
        print(f"Take {end_av} Ave. south for {block1} ft until you get to {end_st} St.")
        print("yay, you've arrived!") 
        
def main(*value):
    print("Starting corner: ")
    print(f"Avenue:", end = '')
    avenue1 = get_positive_integer_input(value)
    print(f"Street:", end= '')
    street1 = get_positive_integer_input(value)

    print("\nEnding corner:")
    print(f"Avenue:", end = '')
    avenue2 = get_positive_integer_input(value)
    print(f"Street:", end= '')
    street2 = get_positive_integer_input(value)

    print()
    
    get_directions(avenue1, street1, avenue2, street2) 

main()


    
