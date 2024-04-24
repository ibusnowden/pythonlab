from turtle import*

"""
for x in range(8):
    forward(100)
    right(45)
"""
NUM_CIRCLES = 10
STARTING_RADIUS = 20
OFFSET = 10
ANIMATION_SPEED = 0

speed(ANIMATION_SPEED)
hideturtle()

radius = STARTING_RADIUS

for count in range(NUM_CIRCLES):
    circle(radius)

    x = xcor()
    y = ycor()

    radius = radius + OFFSET + 1
    penup()
    goto(x, y)
    pendown()
