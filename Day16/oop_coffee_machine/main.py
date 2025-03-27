from src import menu
from src import coffee_maker
from src import money_machine

#item = MenuItem()
menu = menu.Menu()
maker = coffee_maker.CoffeeMaker()
money_machine = money_machine.MoneyMachine()

#Variable to turn off machine
is_off = False

#Coffee machine working
while not is_off:
    drinks = menu.get_items()
    user_input = input(f"What would you like? ({drinks})")
    if user_input == "off":
        #Turn off the coffee machine and exit loop
        is_off = True
    elif user_input == "report":
        #Get report
        money_machine.report()
        maker.report()
    else:
        #Validate that there are enough resources and prepare drink
        chosen_drink = menu.find_drink(order_name = user_input)
        try:
            if maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
                    maker.make_coffee(chosen_drink)
        #If user input is not a valid drink
        except:
            print("Please enter a valid drink option.")