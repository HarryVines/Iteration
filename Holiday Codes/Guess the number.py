#Harry Vines
#10/11/2014
#Guess the number game 

import random

correct = True
random_number = random.randint(0,100)
guesses = 0
while correct==True:
    guess = int(input("Please enter a guess: "))
    if guesses > 10:
        print("GAME OVER! You've had 10 guesses, the correct number was: {0}".format(random_number))
        correct = False
    elif guess > 100 or guess < 0:
              print("Incorrect Value")
    elif guess > random_number:
        print("Your guess is too high")
        guesses = guesses+1
        correct == True
    elif guess < random_number:
        print("Your guess is too low")
        guesses = guesses+1
        correct == True
    elif guess == random_number:
              correct = False
              guesses = guesses+1
              print("You got it right after {0} Guesses!".format(guesses))
              
                    
