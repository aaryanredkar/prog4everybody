score1 = float(input("Enter your score for Science: "))
score2 = float(input("Enter your score for Math: "))
score3 = float(input("Enter your score for Language Arts: "))
score4 = float(input("Enter your score for History: "))
score5 = float(input("Enter your score for PE :"))
score6 = float(input("Enter your score for Wheel: "))

score = score1 + score2 + score3 + score4 + score5 + score6
score = (score / 6)
print("You got", score)

if (score <=59) :
    print("Your grade is F")
elif (score <=69):
    print("Your grade is D")
elif (score <=79):
    print("Your grade is C")
elif (score <=89):
    print("Your grade is B")
elif (score <=100):
    print("Your grade is A")
else:
    print("Error: Invalid Score!!!!!!!!!!!!!! ")
