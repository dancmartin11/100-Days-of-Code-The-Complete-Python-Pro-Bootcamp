#Import required libraries
import random
from art import logo, vs
from game_data import data

#Create function to generate random values for A and B, making sure they are not the same
def get_data():
    '''
    Generate random instagram account data extracting a dictionary value from data list.
    '''
    value = random.choice(data)
    
    return value

#Set values to A and B to play the game
def set_a_b(a, b):
    '''
    Set values to both A and B, which will be the two options for the user to choose in the game.
    '''
    #If it is NOT the first turn, set a previous b value, and get new value for b
    if a is not None:
        a = b
        while a == b: #Make sure we don't get same value for a and b
            b = get_data()
    #If it is the first turn, generate value for both a and b
    elif a is None:
        a = get_data()
        b = get_data()
        while a == b: #Make sure we don't get same value for a and b after both values are assigned for the first time
            b = get_data()
    return a, b
   
#Find the highest value, returning either A or B     
def highest_value(a, b):
    '''
    Finds whether A or B has the highest followers value.
    '''
    if a > b:
        highest = "A"
    else:
        highest = "B"
    return highest
  
#Function containing the game
def higher_or_lower():
    '''
    Executes the game Higher or Lower.
    '''  
    #Set initial variables for the game    
    A = None
    B = None
    score = 0
    wrong  = False
    
    #Execute the game unit user gets wrong
    print(logo)
    while not wrong:
        A, B = set_a_b(A, B)
        highest = highest_value(A['follower_count'], B['follower_count'])
        
        #Print A and B otpions, as well as UI
        print(f"Compare A: {A['name']}, {A['description']} from {A['country']}.")
        print(vs)
        print(f"Against B: {B['name']}, {B['description']} from {B['country']}.")
        
              #Ask user to guess for the highest
        guess = input("Who has more followers? Type'A' or 'B': ").upper()
        
        #Validate if user got it right
        if guess == highest:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            wrong = True

#Execute the game
exit_game = False
while not exit_game:
    higher_or_lower()
    
    #Validate if player wants to play again
    another_game = input("Do you want to play again? Type 'Y' o start a new game.").upper()
    if another_game != "Y":
        print("Goodbye!")
        break