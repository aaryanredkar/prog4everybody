limit = int(input("Enter the upper limit for fibbonaci :"))
a,b =0,1
print("0")
while b < limit:
    print(b)
    a,b = b, a+b
