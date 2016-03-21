#This program will print Nth number
#that is divisible by 3
n = int(input("Enter the Nth number divisible by 3 : "))
count = 1
i = 1
while (True):
    if(i%3==0):
        if count==n:
            print(n,"number divisible by 3 is:",i)
            break
        else:
            count= count+1
    i = i+1
