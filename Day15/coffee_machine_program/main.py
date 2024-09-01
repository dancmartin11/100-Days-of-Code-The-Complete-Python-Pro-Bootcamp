# Import required libraries


# Function that takes user's order
def take_order(menu: dict) -> str:
    """
    Function that prompts the user what drink do they want from the coffee machine, returning their selection.
    >*Note: There are valid secret input for the maintainers of the coffee machine. "report" provides the amount of resources in the
    coffee machine, while "off" turns off the machine.*
    ---
    Args:
        menu(dict): Dictionary with the information about all the available drinks in the coffee machine.
    Returns:
        str: Chosen drink by the customer or maintenance command for the coffee machine to proceed.
    """
    # Available drinks in the machine
    drinks = list(menu.keys()) + ["report", "off"]

    # Ask user to input the drink they want (will loop in case they type an invalid option)
    chosen_drink = ""
    while chosen_drink not in drinks:
        chosen_drink = input("What would you like? (espresso/latte/cappuccino):").lower().strip()

    return chosen_drink

#Function that prints out the report with the current inventory values
def get_report(resources: dict) -> str:
    """
    Generate the report for the current inventory of the resources in the coffee machine.
    ---
    Args:
        resources (dict): Dictionary containing the amount of resources in the coffee machine (water, milk, coffee and money).

    Returns:
        str: Formatted report with resources values as a string, can be printed out.
    """    
    report = f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}'
    
    return report

def check_resources(menu: dict, resources: dict, chosen_drink: str) -> bool:
    """
    Function that validates if there are enough resources to prepare the ordered drink.
    ---
    Args:
        menu (dict): Dictionary containing the available drinks with the required resources and their amounts.
        resources (dict): Dictionary containing the current machine's resources.
        chosen_drink (str): Drink that was ordered by the user.

    Returns:
        bool: True or False determining whether there are enough resources or not. If some resource is missing, it will also print out which one.
    """    
    #Initialize boolean variable for validation
    enough_resources = True
    
    #Check for required resources and compare their amount to the machine's resources
    for key, val in menu[chosen_drink]["ingredients"].items():
        if val > resources[key]:
            enough_resources = False
            print(f"Sorry there is not enough {key}.")
            break
        
    return enough_resources

'''
COFFEE MACHINE
'''
#Menu of available drinks
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,  
    },
    "latte":{
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#Initialize coffee machine
turn_off = False

#Initial resources
machine_resources = {"water": 200,
                     "milk": 200,
                     "coffee": 100,
                     "money": 10,
}

#Run orders until machine gets turned off by maintenance staff
while not turn_off:
    #Ask for users to input the drink they want
    drink = take_order(MENU)
    #Flow for users requesting drinks
    if drink != 'off' and drink != 'report':
        print(drink)
        #Validate that there are enough resources in teh machine
        resource_val = check_resources(MENU, machine_resources, drink)
        print(resource_val)
    #Flow for getting resource report
    elif drink == 'report':
        print(get_report(machine_resources))
    #Flow for turning off the coffee machine
    else:
        turn_off = True
        print('Goodbye!')
