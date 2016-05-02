def is_prime(count):
    for x in range(2, count):
        if count% x ==0:
            print (count, "is not a prime number")
            break
    else:
        print(count,"is a prime number")

limit = int(input("Pleasse enter a +ve integer?"))
is_prime(limit)
