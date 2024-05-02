print('Reboot the computer and try to connect.')
enter = input('Did that fix the problem? ')

if enter == 'no':
    print('Reboot the router and try to connect.')
    
    enter = input('Did that fix the problem? ')
    if enter == 'no':
        print('Make sure the cable between the router and modem are plugged in firmly')
        
        enter = input('Did that fix the problem? ')
        if enter == 'no':
            print('Move the router to a new location.')
            
            enter = input('Did that fix the problem? ')
            if enter == 'no':
                print('Get a new router')
        else:
            if enter == 'yes':
              print('')
    else:
        if enter == 'yes':
            print('')

else:
    if enter == 'yes':
        print('')    