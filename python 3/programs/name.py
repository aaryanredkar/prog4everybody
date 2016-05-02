name = input("Enter your complete name....")

try:
    index_of_space =name.index(" ")
except ValueError:
    print('Please provide both both first name and last name')
else:
    print('Your name is:')
    print(name[:index_of_space])
    print(name[index_of_space+1:])
    
