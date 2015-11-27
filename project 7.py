s1 = int(input("Science score:"))
s2 = int(input("Math score:"))
s3 = int(input("Language score:"))
s4 = int(input("History score:"))
s5 = int(input("PE score:"))
s6 = int(input("Music score:"))
sum = (s1 + s2 + s3 + s4 +s5 +s6)/6
print("Your avarage score is : ", sum)


if sum <= 59:
      print ("The score is an F")
elif sum <= 69:
      print ("The score is an D")
elif sum<= 79:
      print("The score is an C")
elif sum<= 89:
      print("The score is an B")
elif sum<= 99:
      print("The score is an A")


      
