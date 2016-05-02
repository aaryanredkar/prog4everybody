name = input("Enter your name:")
name=name.lower()
vowels=['a','e','i','o','u']
count=0
for letter in name:
    if(letter in vowels):
        count=count+1

print ("Total number of vowels in your name:",count)
