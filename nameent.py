def print_name(user_name,number_of_times):
    for i in range (1,number_of_times + 1):
        print (user_name)
name = input("What is your name:")
num= int(input("How many times do you want your name to be printed:"))
#fname= name*num + " "
#space = (" ")
#print (fname)
print_name(name, num)



