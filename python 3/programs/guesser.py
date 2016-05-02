import random

guessesLeft = 10
userName = input("Please enter your Name :")
number = random.randint(1, 10)
print("Hello",userName,"I'm thinking of a number between 0 and 10")

while guessesLeft>0:
    print("You have",guessesLeft,"guesses left")
    guess = int(input("guessa number: "))
    guessesLeft = guessesLeft - 1
    if guess < number:
        print("your guessis toolow.")
    elif guess >number:
        print("Your guess is too high")
    elif guess==number:
        print("good job,",userName,"!You guessed my number in",(10-guessesLeft),"guesses!")
        break
    if guessesLeft==0:
        print("Sorry.The number I was thinking of was", number)
        break
print("Have a Nice Day...") 
