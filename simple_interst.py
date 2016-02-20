def Simple_Interest(P,i,t):
   
    I=P*t*(i/100)
    return I
P=int(input("enter Principal:"))
i=int(input("enter Percentage of interest rate:"))
t=int(input("enter Time(in years):"))
s = Simple_Interest(P,i,t)
print ("Interest is", s,"dollars")


  
