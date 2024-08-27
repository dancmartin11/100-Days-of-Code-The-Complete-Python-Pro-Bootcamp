############### Blackjack Project: Daniel Alejandro Castillo Martin #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo

#Create function that will execute the game
def blackjack():
    deck = {
      "Ace": 11,
      "2": 2,
      "3": 3,
      "4": 4,
      "5": 5,
      "6": 6,
      "7": 7,
      "8": 8,
      "9": 9,
      "10": 10,
      "Jack": 10,
      "Queen": 10,
      "King": 10
    }

    start_game = input("Do you want to play a game of Backjack? Type 'y' or 'n': ").lower()

    if start_game == "y":

        #Initialize lists where user and computer's cards will be stored
        user_cards = []
        user_score = 0

        computer_cards = []
        computer_score = 0

        #Create variable to validate the starting position of aces
        user_ace_pos = 0
        computer_ace_pos = 0

        #Clear the screen every time a new game is started and print the blackjack logo
        clear()
        print(logo)

        #Get the first two cards for the user and computer
        for _ in range(2):
            user_cards.append(random.choice(list(deck.keys())))
            computer_cards.append(random.choice(list(deck.keys())))

        #Get first scores for user and computer, validate if there are two Aces
        for card in user_cards:
            user_score += deck[card]
            #In case user gets initially two Aces
            if user_score > 21:
                user_score -= 10
                ace_pos += 1

        for card in computer_cards:
            computer_score += deck[card]
            #In case user gets initially two Aces
            if computer_score > 21:
                computer_score -= 10
                computer_ace_pos += 1

        #Continue the game while scores are below 21
        while user_score < 21 and computer_score < 21:

            print(f"Your cards: {user_cards}, current score: {user_score}.")
            print(f"Computer's first card: {computer_cards[0]}.")

            #Ask user if wants another card
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            #Append cards if user wants another one
            if another_card == "y":

                user_cards.append(random.choice(list(deck.keys())))
                user_score += deck[user_cards[-1]]

                computer_cards.append(random.choice(list(deck.keys())))
                computer_score += deck[computer_cards[-1]]

                #If score is above 21, validate if there are any Aces
                if user_score > 21:
                    for card in user_cards[user_ace_pos:]:
                        if card == "Ace":
                            user_score -= 10
                            if user_score <= 21:
                                break

                if computer_score > 21:
                    for card in computer_cards[computer_ace_pos:]:
                        if card == "Ace":
                            computer_score -= 10
                            if computer_score <= 21:
                                break

            #If user does not want another card, let the computer play until its score is above 17
            elif another_card == "n":
                while computer_score < 17:
                    computer_cards.append(random.choice(list(deck.keys())))
                    computer_score += deck[computer_cards[-1]]

                    #If score is above 21, validate if there are any Aces
                    if computer_score > 21:
                        for card in computer_cards[computer_ace_pos:]:
                            if card == "Ace":
                                computer_score -= 10
                                if computer_score <= 21:
                                    break

                #If anyone went over, check out scores
                if computer_score < 21:
                    print(f"Your final hand: {user_cards}, final score: {user_score}.")
                    print(f"Computer's final hand: {computer_cards}, final score {computer_score}.")
                    
                    if user_score > computer_score:
                        print("You win.")
                    elif user_score == computer_score:
                        print("It's a draw.")
                    else:
                        print("You lose.")
                    break
            #Ask the user again in case they wrote an invalid character
            else:
            continue

        #Print result if user went over
        if user_score > 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}.")
            print(f"Computer's final hand: {computer_cards}, final score {computer_score}.")
            print("You went over. You lose!")

        #Print result if computer went over
        elif user_score < 21 and computer_score > 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}.")
            print(f"Computer's final hand: {computer_cards}, final score {computer_score}.")
            print("The dealer went over. You win!")

        #If user got BlackJack...
        elif user_score == 21:
            #Let computer play until its score is above 17
            while computer_score < 17:
                computer_cards.append(random.choice(list(deck.keys())))
                computer_score += deck[computer_cards[-1]]

                #If score is above 21, validate if there are any Aces
                if computer_score > 21:
                    for card in computer_cards[computer_ace_pos:]:
                        if card == 'Ace':
                            computer_score -= 10
                            if computer_score <= 21:
                                break

            print(f"Your final hand: {user_cards}, final score: {user_score}.")
            print(f"Computer's final hand: {computer_cards}, final score {computer_score}.")

            #If computer also got BlackJack, user loses
            if computer_score == 21:
                print("Dealer got a Blackjack! You lose!")
            #If user did not get BlackJack, user wins
            else:
                print("You got a Blackjack! You win!")

        #If computer got BlackJack, automatically wins
        elif computer_score == 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}.")
            print(f"Computer's final hand: {computer_cards}, final score {computer_score}.")
            print("Dealer got a Blackjack! You lose!")

        #Ask the user if wants to play another game
        blackjack()

    elif start_game == "n":
        print("Goodbye!")

    else:
        blackjack()


#Execute the game
blackjack()