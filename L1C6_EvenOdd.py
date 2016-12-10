number=int(input("Please enter the ending number:"))
##Logic 1
print("All the even Number <=",number,"are:")
for i in range (1, number+1):
    if(i%2==0):
        print(i,"is even number")

print("All the odd Number <=",number,"are:")
for i in range(1,number+1):
    if(i%2==1):
        print(i,"is odd number")
