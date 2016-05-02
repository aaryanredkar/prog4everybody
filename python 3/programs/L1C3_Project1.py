# If Condition Example

x = int(input("Please enter an integer:  "))
if x == 0:
    print("Value entered is Zero")
elif x > 0:
    print("Value entered is Positive Integer")
elif x < 0:
    print("Value entered is Negative Integer")
else:
    print('Well this should never be printed!!!')
