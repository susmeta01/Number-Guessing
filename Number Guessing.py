import random

n = random.randrange(1,101)
guess = 9
print ("\nWelcome to the number guessing game!\nGuess the number between 1 to 100\nYou have 9 guesses\n")
while (guess != 0):
    num = int(input("Guess a number : "))
    if (num < n):
        print ("Guess a higher number")
    elif (num > n):
        print ("Guess a lower number")
    elif (num == n):
        print ("Congratulations! You guessed it ")
        break
    guess = guess - 1
    print("You have "+ str(guess) + " guesses left\n")
if (guess == 0):
    print("Game Over ! :( \nThe number was ", n)
