Value = int(input("Give me a number which will be the limit of fib sequence"))
print ("The fibonnaci sequence<=",Value, "is: ")
a, b = 0,1
temp = 0
print ("0")
while (b <= Value):
    print (b)
    temp = a+b
    a = b
    b = temp
