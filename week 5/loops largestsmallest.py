largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done" : break
	try:
		s = int(num)
		if s > largest :
			largest = s
			
		if s < smallest or smallest == None :
			smallest = s

		
	except:
		print "Invalid input"


print "Maximum is", largest

print "Minimum is", smallest
