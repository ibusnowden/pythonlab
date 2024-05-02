import shapes

X1 = 0
Y1 = 100
X2 = -100
Y2 = -100
X3 = 100
Y3 = -100
RADIUS = 50

def main():
    shapes.sqaures(X2, Y2, (X3-X2), 'yellow')

    shapes.circle(X1, Y1, RADIUS, 'blue')
    shapes.circle(X2, Y2, RADIUS, 'red')
    shapes.circle(X3, Y3, RADIUS, 'green')
