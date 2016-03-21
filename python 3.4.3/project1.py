i = input("what is your name?")
i = i.lower()
vowels= ['a', 'e','i' ,'o','u']
count = (0)
for letter in i:
    if(letter in vowels):
        count = count +1

print("Total number of vowels in your name:", count)


