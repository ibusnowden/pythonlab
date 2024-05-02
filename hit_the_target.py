from turtle import*

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target
hideturtle()
speed(0)
penup()
goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
pendown()
setheading(EAST)
forward(TARGET_WIDTH)
setheading(NORTH)
forward(TARGET_WIDTH)
setheading(WEST)
forward(TARGET_WIDTH)
setheading(SOUTH)
forward(TARGET_WIDTH)
penup()

# Center the turlte
goto(0, 0)
setheading(EAST)
showturtle()
speed(PROJECTILE_SPEED)

angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))
distance = force * FORCE_FACTOR

setheading(angle)

pendown()
forward(distance)

if (xcor() >= TARGET_LLEFT_X and
    xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    ycor() >= TARGET_LLEFT_Y and
    ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Target hit!')
else:
    print('You missed the target')
    if xcor() > (TARGET_LLEFT_X + TARGET_WIDTH):
        print('Increase your angle')
    elif xcor() < TARGET_LLEFT_X:
        print('Decrease your angle')
    if ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH):
        print('Decrease your force')
    elif ycor() < TARGET_LLEFT_Y:
        print('Increase your force')


# End of the program
#done()












