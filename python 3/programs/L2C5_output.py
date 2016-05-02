import math
name= "Jack"
age= 8
print("My name is %s and I am %d years old. Pi is %0.4f." % (name, age, math.pi))

name = "John"
age = 6
print("My name is", name, "and I am", age, "years old.")


print("My name is {} and I am {} years old.".format("Kevin",11))

print("My name is {0} and I love {1}".format("Messi", "Soccer"))
print("My name is {1} and I love {0}".format("Messi", "Soccer"))

print("My name is {player} and I love {game}".format(game="Soccer", player="Messi"))
print("My name is {player} and I love {game:6.4f}".format(game= math.pi,player="Messi"))

