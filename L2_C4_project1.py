num = int(input("What is the number"))

if (num < 2):
    print("Invalid number" , num)
else:
    print("Prime numbers:")
    for i in range(2, num + 1):
        for j in range (2, i):
            if(i%j == 0):
                break

        else:
            print(i)


    print("That's it............")
