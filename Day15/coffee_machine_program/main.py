#Import required libraries
from core.coffee_machine import CoffeeMachine
from data import menu_data, coin_data

#Initialize menu and coin data
COINS = coin_data.coins
MENU = menu_data.menu

#Execute the Coffee Machine program
CoffeeMachine(menu_dict = MENU,
              coins_dict = COINS,
              water_amount = 10000,
              milk_amount = 10000,
              coffee_amount = 500,
              money_amount = 1000)