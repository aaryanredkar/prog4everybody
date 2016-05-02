mylist= ["Math" , "Science","History", "Core", "PE"]

print ("mylist[1]",mylist[1])
print ("mylist[-1]", mylist [-1])

print ("/nAppend one more item to thelist....")

mylist.append("Computer")
print(mylist[-1])

print("/nAdd one item at index2....")

print ("mylist [2]",mylist [2])

mylist.insert(2, "Geology")
print ("/nPrint Index of element History....")
print(mylist.index("History"))

print ("/nSort and print the list....")
mylist.sort();
for item in mylist:
    print (item)

print ("/nReverse and print the list....")
mylist.reverse();
for item in mylist:
    print(item)

print ("/nRemoveone item from the list....")
mylist.remove("PE")
for item in mylist:
    print (item)

print ("/nClear the entire list....")
mylist.clear
for item in mylist:
    print (item)
