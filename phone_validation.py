def is_valid_phone_number(string):
    if len(string) == 14 and (string[0] + string[1]) == '1-':
        digits = string[2:].split('-')
        if len(digits) == 3 and all(d.isdigit() for d in digits):
            print('True')
    
    elif len(string) == 10 and string.isdigit():
        print('True')
    
    elif len(string) == 12:
         digits = string[2:].split('.')
         if len(digits) == 3 and all(d.isdigit() for d in digits):
            print('True')
    
    else:
        print('False')
      
is_valid_phone_number('1-800-867-5309')
is_valid_phone_number('800.867.5309')
is_valid_phone_number('8008675309')
is_valid_phone_number('8oo-867-53o9')
is_valid_phone_number('800*867*5309')

