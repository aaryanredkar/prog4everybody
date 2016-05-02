import mylib

val = int(input(" Enter 1-Simple Interest,2-command""and 3-Celsius to fahrenheit cnversion:"))

if (val ==1 or val== 2):
    startamount = float(input("Please enter the Principal Amount in $"))
    interest_rate = float(input("Please enter the Interest Rate"))
    years = int(input("pleaseenter the time in years"))
    if (val==1):
        print(mylib.simpleInterest (startamount, interest_rate, years))
    else:
        print(mylib.compoundInterest (startamount, interest_rate, years))
elif (val ==3):
    temp= float(input("Please enter the temp in calsius:"))
    print (mylib.c2f(temp))
else:
    print("Invalid value!!")
