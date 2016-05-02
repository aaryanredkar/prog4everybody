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
    if students <= 25:
        t.fillcolor("red")
    elif students < 75 and students > 25:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    makeBar(t, students, year)

percent_of_kids_like = [60, 90, 20, 50, 80]
food= ["Pizza", "Candies", "Vegetables", "Chips", "Ice Cream"]

max_height = max(percent_of_kids_like)
num_bars = len(percent_of_kids_like)
border = 10

graphMaker = turtle.Turtle()
graphMaker.pensize(5)

bg = turtle.Screen()
bg.bgcolor("lightgreen")
bg.setworldcoordinates(0,0,40*num_bars+border,max_height+border)

for i in range (len(percent_of_kids_like)) :
    selectColor(graphMaker,percent_of_kids_like[i],food[i])

bg.exitonclick()

    
