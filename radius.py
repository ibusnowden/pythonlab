from turtle import*

NUM_CIRCLES = 5
STARTING_RADIUS = 25
ANIMATION_SPEED = 0
OFFSET = 5

speed(ANIMATION_SPEED)
hideturtle()

radius = STARTING_RADIUS

count = 1
while count <= NUM_CIRCLES:
    circle(radius)
    radius = radius + OFFSET
    x = xcor()
    y = ycor() - OFFSET
    
    penup()
    goto(x, y)
    pendown()

    count  = count + 1


