print ("all amounts should be in dollars!")

while True:
	P=int(input("enter Principal:"))
	i=int(input("enter Percentage of interest rate:"))
	t=int(input("enter Time(in years):"))
	I=P*t*(i/100)
	print ("Interest is", I,"dollars")
