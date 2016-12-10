import turtle
shape = turtle.Turtle()

shape.pencolor("blue")


for i in range(50):
    shape.fd(50)
    shape.lt(123)


shape.pencolor("red")
for i in range(50):
    shape.fd(100)
    shape.it(123)

turtle.done()
