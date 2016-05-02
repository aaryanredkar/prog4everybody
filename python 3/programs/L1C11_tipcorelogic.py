amount = int(input("Please enter the total bill amount:"))
tip = int(input("Enter tip rate:"))


total_bill = amount + (amount * tip/100)


print ("Your total bill is:",total_bill)
people = int(input("How many people are in your party?:"))


print ("Each person should pay $",total_bill/people)
