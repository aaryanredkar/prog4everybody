n = int(input("Give me the highest number to print all the digits divided by three:"))  
for number in range(1,n + 1):
    if number % 3 == 0: 
         print(number)
