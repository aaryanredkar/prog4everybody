import turtle
spiral = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightgreen")

shape = turtle.Turtle()
shape.shape("line")
shape.color("blue", "green")


shape.penup()
size= 25
for i in range(30):
    spiral.fd(i*10)
    spiral.rt(144)
    shape.stamp()
    size = size + 3
    shape.forward(size)
    shape.right(24)
    

screen.mainloop()

turtle.done()
