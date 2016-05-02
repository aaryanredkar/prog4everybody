import turtle

shape = turtle.Turtle()
shape.pencolor("blue")

value = int(input("Please enter MaxValue for Fibonnaci sequence:"))

a, b = 0, 1
temp = 0
print("0 ")
while (b<= value):
    shape.circle(b)
    temp= a+b
    a = b
    b = temp

turtle.done()
