import turtle

turtle.speed(12)
turtle.color('light green')
turtle.bgcolor('black')

b = 200
while b > 0:
    turtle.left(b)
    turtle.forward(b * 3)
    b -= 1

turtle.done()
