# Number guessing game
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number
# If user guessed it correctly then print "You won"
# If user didn't guessed correctly then #if user guessed lower than actual number, print "too low"
#if user guessed higher than actual number, print "too high"
# Use google to find how to generate random no.
# import random
winning_number=27
guess=input("Guess the number between 1 and 100:\n")
guess=int(guess)
if guess == winning_number:
    print("Yes, you won")
else:
    if(guess > winning_number):
        print("Too high")
    else:
        print("too low")
    


