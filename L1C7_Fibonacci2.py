# While Loop to generate Fibonacci series:
limit =int(input("Enter the upper limit for Fibonacci : "))
a, b = 0, 1
print("0")
while b < limit:
    print (b)
    a, b = b, a+b
