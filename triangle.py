import turtle

def main():
  drawing = triangle(5, 4, 'green')
  
def triangle(X, Y, color):
  turtle.fillcolor(color)
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(X, Y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(3):
      turtle.forward(100)
      turtle.left(120)
      turtle.forward(100)
      turtle.hideturtle()
  turtle.end_fill()

main()

