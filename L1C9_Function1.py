# Prime Number Logic
def is_prime (count):
    for x in range (2,count):
        if count % x == 0:
            print(count,"is NOT a prime number")

limit = int(input("Please enter a +ve integer: "))
is_prime(limit)
