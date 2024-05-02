menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS'] 

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination
            
    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print(f'{passenger.title()} --> {passengers[passenger]}')
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()
  
"""
string note
    
    # Methods to create new strings: 
    replace(old, new) —Returns a copy of the string with all occurrences of the substring old replaced by the string new. The old and new arguments may be string variables or string literals.
    replace(old, new, count) -- Same as above, except replace(old, new, count) only replaces the first count occurrences of old.
    capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
    lower() -- Returns a copy of the string with all characters lowercased.
    upper() -- Returns a copy of the string with all characters uppercased.
    strip() -- Returns a copy of the string with leading and trailing whitespace removed.
    title() -- Returns a copy of the string as a title, with first letters of words capitalized.

    # Methods to check a string value that returns a True or False Boolean value: 
    isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
    isdigit() -- Returns True if all characters are the numbers 0-9.
    islower() -- Returns True if all cased characters are lowercase letters.
    isupper() -- Returns True if all cased characters are uppercase letters.
    isspace() -- Returns True if all characters are whitespace.
    startswith(x) -- Returns True if the string starts with x.
    endswith(x) -- Returns True if the string ends with x.
    
    # Some methods are useful for finding the position of where a character or substring is located in a string: 
    find(x) -- Returns the index of the first occurrence of item x in the string, otherwise, find(x) returns -1. x may be a string variable or string literal.
    find(x, start) —Same as find(x), but begins the search at index start: 
    find(x, start, end) -- Same as find(x, start), but stops the search at index end - 1: 
    rfind(x) -- Same as find(x) but searches the string in reverse, returning the last occurrence in the string.
    count(x) -- Returns the number of times x occurs in the string. 

  #############
  replacement = input()
tongue_twister = input()

''' Your code goes here '''
if replacement in tongue_twister:
    i = tongue_twister.find(replacement)
    r = tongue_twister.replace(replacement, '--', 3)
    print('Located at index:', i)
    print(r)
else:
    print('Not available')
  """