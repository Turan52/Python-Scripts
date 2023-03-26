import turtle

t = turtle.Turtle()

width = 100
height = 50
angle = 30

t.penup()
t.goto(0, 0)
t.pendown()

t.forward(width)
t.left(angle)
t.forward(height)
t.left(180 - angle)
t.forward(width)
t.left(angle)
t.forward(height)

turtle.done()