#modules always contain functions
import math

def simpleInterest(initial_amount, rate, time):
    return initial_amount + (initial_amount* (rate/100) *time)

def compoundInterest(initial_amount, rate, time):
    return  (initial_amount *math.pow(1 + (float(rate)/100),time))
             
def c2f(temp):
        return   (temp* 9/5) +32
