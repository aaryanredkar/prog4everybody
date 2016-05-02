import turtle

side = int(input("Enter the side of the triangle : "))


turtle.pensize(1)
turtle.color("red")

turtle.fd(side)
turtle.lt(120)
turtle.fd(side)
turtle.lt(120)
turtle.fd(side)


turtle.exitonclick()
