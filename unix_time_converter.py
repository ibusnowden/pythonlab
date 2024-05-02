# the number of second in 1 day
SECONDS = 86400
# The number of seconds in 1 hour
HOURS_SECONDS = 3600
# The numbr of second in 1 minute
M_SECONDS = 60

t_time = int(input("Enter a Unix time: "))
t_days = t_time // SECONDS

n =  t_time % SECONDS
t_hours = (n * 24) // SECONDS

n = t_time % HOURS_SECONDS
t_minutes = (n * 60) // HOURS_SECONDS

n = t_time % M_SECONDS
t_seconds = (n * 60) // M_SECONDS

print('\nThat is')
print(f'{t_days} days(s)')
print(f'{t_hours} hour(s)')
print(f'{t_minutes} minute(s)')
print(f'{t_seconds} second(s)')

