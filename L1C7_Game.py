import random


guessesLeft = 15
userName = input("Please enter your Name :")
number = random.randint(1, 1000)
print("Hello", userName, "I'm thinking of a number between 0 and 1000.")

while guessesLeft > 0:
    print("You have", guessesLeft, "guesses left")
    guess = int(input("Guess a number : "))
    guessesLeft = guessesLeft - 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    elif guess == number:
        print("Good job,",userName,"! You guessed my number in",(15-guessesLeft),"guesses!")
        break
    if guessesLeft == 0:
        print("Sorry. The number I was thinking of was", number)
        break


print("Have a Nice Day...")
