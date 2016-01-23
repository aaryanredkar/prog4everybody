n = int(input("Enter any number to check for palindrome:"))
temp= n
remainder = reverse = 0
while (temp > 0) :
    remainder = temp % 10
    temp = temp / 10
    reverse = reverse *10 + remainder
if(int(temp) == reverse):
    print ("Given number " +str(n)+" is palindrome")
else:
    print ("Given number " +str(n)+" is not a palindrome")
   
