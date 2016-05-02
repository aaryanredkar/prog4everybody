print ("THis Python program will calculate money in your piggy bank...")
options = ["Dollar Coins ","Fifty Cents", "Quaters", "Dime", "Nickels", "Pennies"]
multi_factor= [1, 0.5,0.25,0.1, 0.05, 0.01]

for i in range (len(options)):
    coins = int(input( "How many of {} do you have:".format(options[i])))
    total = total+ (coin * multi_factor[i])
print("Total money $[0]".format(total))
