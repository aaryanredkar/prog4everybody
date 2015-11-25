hrs = raw_input("Enter hours:")
h = float(hrs)
r = raw_input("Enter rate:")
rate = float(r)

if h <= 40 :
	#print "rate:" + str(rate)
	#print "hours:" + str(h)
	pay = rate* h 

else :
	pay = rate * 40 + ( rate * 1.5 *(h - 40) )

print pay