
def factorial(number):
    total = 1
    for i in range (1,number+1):
        total = total * i

    return total

print (factorial(5))
