string =input("Enter any string to check if it is Palindrome or not :")

if( string  == string[::-1]):
    print("{} is Palindrome".format(string))
else:
    print("{} is not Palindrome".format(string))
