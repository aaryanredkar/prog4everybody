mylist =[]
for i in range(6):
    name = input ("Please enter the first an last name:")
    mylist.append(name)

for element in mylist:
    print(element)

print ("/nlist in ascending order")
mylist.sort()
for element in mylist:
    print (element)

print ("/n List in Descending order")
mylist.reverse()
for element in mylist:
    print (element)
