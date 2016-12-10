#The password is 123456789.
age = int(input("Enter your age: "))
if (age > 8):
    password = int(input("Enter your Password (numbers only)... "))
    if (password == 123456789):
        print("Access Granted...")
    else:
        print("Invalid Password")
else:
    print("You are a minor and are not allowed to enter :-(")
