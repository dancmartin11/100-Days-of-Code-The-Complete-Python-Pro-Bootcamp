########## GUESS THE NUMBER! ###################3

def get_lives(game_difficulty): 
    '''
    Determines the number of lives the user has when selecting difficulty.
    '''
    n_lives = {'easy': 10, 'hard': 5}    
    return n_lives[game_difficulty]

def get_number():
    '''
    Generates a random number, which the user will try to guess in the game.
    '''
    number = random.randint(1,100)
    return number


def guess_the_number():
    '''
    Executes the game "Guess the Number!"
    '''
    #Print out the on boarding of the game
    print(logo,"\n", 'Welcome to the Number Guessing Game!', "\n", "I'm thinking of a number between 1 and 100.") 
    
    #Set game difficulty and assign lives to the user
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    while difficulty not in ['easy', 'hard']:
        difficulty = input("Please enter a valid difficulty. Type 'easy' or 'hard': ").lower()
    
    lives = get_lives(difficulty)
    
    #Generate random number for starting the game
    rand_number = get_number()
    #print(f"Pssst, the correct answer is {rand_number}") #Coment this line, it's only for testing!!!!
    
    #Time for the user to guess for the number!
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Please enter a valid number.")
            continue
        
        if guess == rand_number:
            print(f"You got it! The answer was {rand_number}.")
            break
        elif guess < rand_number:
            lives -= 1
            print("Too low.")
        elif guess > rand_number:
            lives -= 1
            print("Too high.")
    
        #Still have lives?
        if lives > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")

#Import required objects
from art import logo
import random

#Create exit variable for exiting the game
exit = False

#Execute the game until the user does not want to play anymore
while not exit:  
    guess_the_number()
    
    #Ask the user if he/she wants to play another game
    another_game = input("Do you want to play again? Type 'y' to play again: ").lower()
    
    if another_game == 'y':
        continue
    else:
        print('Goodbye!')
        exit = True