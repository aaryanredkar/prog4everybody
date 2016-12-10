import turtle

side = int(input("Enter the side of the star:"))

mystar = turtle.Turtle()


for i in range(5):
    mystar.fd(side)
    mystar.rt(144)
