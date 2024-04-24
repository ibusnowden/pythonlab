import turtle

def main():
    turtle.hideturtle()
    square(0, 0, 100, 'red')
    square(-150, -75, 200, 'blue')
    square(-200, 150, 75, 'green')

def square(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y-radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(radius)
        turtle.left(90)
    turtle.end_fill()

main()
