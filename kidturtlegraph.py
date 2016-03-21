import turtle

def makeBar(t, students, food):
    t.begin_fill()
    t.write(str(food))
    t.left(90)
    t.forward(students)
    t.write(str(students))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(students)
    t.left(90)
    t.end_fill()                 

def selectColor(t, students, food):
    if students >=1000:
        t.fillcolor("red")
    elif students >= 500 and students < 1000:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    makeBar(t, students, food)

students = [20, 50, 60, 80, 90]
food = ["vegetables", "chips", "pizza", "ice-cream", "candies"]

max_height = max(students)
num_bars = len(students)
border = 10

graphMaker = turtle.Turtle()        
graphMaker.pensize(5)

bg = turtle.Screen()            
bg.bgcolor("white")
bg.setworldcoordinates(0,0,40*num_bars+border,max_height+border)

for i in range (len(students)) :
    selectColor(graphMaker,students[i],food[i])

bg.exitonclick()
