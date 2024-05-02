import turtle

def triangle(X1, Y1, X2, Y2, X3, Y3, color):
  turtle.fillcollor(color)
  turtle.hideturtle()
  turtle.penup()
  turtle.goto(X1, Y1)
  turtle.pendown()
  turtle.begin_fill()
  turtle.goto(X2, Y2)
  turtle.goto(X3, Y3)
  turtle.goto(X1,Y1)
  turtle.end_fill()

triangle()


