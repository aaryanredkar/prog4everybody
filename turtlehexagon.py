

from turtle import *
setup()
x = 0
# Use your own value
y = 0
# Use your own value
length = int(input("What is the length:"))
def hexagon (size_length):
    #penup()
    pendown ()
    forward(size_length)
    right (60)

goto (x, y) 
for _ in range (6):
    hexagon (length)             

exitonclick ()
