import turtle

def makeBar(t, students, year):
    t.begin_fill()
    t.write(str(year))
    t.left(90)
    t.forward(students)
    t.write(str(students))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(students)
    t.left(90)
    t.end_fill()

def selectColor(t, students, year):
    if students >=1000:
        t.fillcolor("red")
    elif students >=500 and students < 1000:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    makeBar(t, students, year)

students = [300, 396, 500, 750, 1400]
year = [1995, 2000, 2005, 2010, 2015]

max_height = max(students)
num_bars = len(students)
border = 10

graphMaker = turtle.Turtle()
graphMaker.pensize(5)

bg = turtle.Screen()
bg.bgcolor("lightgreen")
bg.setworldcoordinates(0,0,40*num_bars+border,max_height+border)

for i in range (len(students)) :
    selectColor(graphMaker,students[i],year[i])

bg.exitonclick()

    
