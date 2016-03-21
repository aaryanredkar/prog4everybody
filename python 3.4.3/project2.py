dollar = int (input("How many 1-dollar"))
D = int(input("How many dollars do you have"))
half = int(input("How many half do you have"))
Quater = int(input("How many quaters do you have"))
dimes = int(input("How many dimes do you have"))
nickels= int(input("How many nickels do you have"))
pennies = int(input("How many pennies do you have"))

total = D *1 + half * 0.5 + Quater * 0.25 + dimes * 0.10 + nickels *0.05 + pennies * 0.01
print ("Total money in bank ${0:.2f}".format(total))
