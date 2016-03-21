import turtle 
length = int(input("How long should the spiral be:"))
ninja = turtle.Turtle()

ninja.speed(10)
pink = ninja.pencolor("pink")
blue = ninja.pencolor("blue")
red = ninja.pencolor("blue")
yellow = ninja.pencolor("yellow")
green= ninja.pencolor("green")

    
for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(length)
    
turtle.done()
