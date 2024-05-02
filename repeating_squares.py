from turtle import*

LENGTH = 5
NUM_SQUARES = 100
OFFSET = 2
hideturtle()
speed(10)

for x in range(100):
   for m in range(4):
     left(90)
     forward(LENGTH)
   LENGTH = LENGTH + OFFSET

