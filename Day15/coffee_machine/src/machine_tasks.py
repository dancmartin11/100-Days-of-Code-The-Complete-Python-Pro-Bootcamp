class MachineTasks:
    def __init__(self):
        pass
    # Function that takes user's order
    def take_order(self, menu_dict: dict) -> str:
        """
        Function that prompts the user what drink do they want from the coffee machine, returning their selection.
        >*Note: There are valid secret input for the maintainers of the coffee machine. "report" provides the amount of resources in the
        coffee machine, while "off" turns off the machine.*
        ---
        Args:
            menu_dict (dict): Dictionary with the information about all the available drinks in the coffee machine.
        Returns:
            str: Chosen drink by the customer or maintenance command for the coffee machine to proceed.
        """
        # Available drinks in the machine
        drinks = list(menu_dict.keys()) + ["report", "off"]

        # Ask user to input the drink they want (will loop in case they type an invalid option)
        chosen_drink = ""
        while chosen_drink not in drinks:
            chosen_drink = input("What would you like? (espresso/latte/cappuccino):").lower().strip()

        return chosen_drink

    #Function that prints out the report with the current inventory values
    def get_report(self, resources: dict) -> str:
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

    #Function that validates that there are enough resources to prepare the drink
    def check_resources(self, menu_dict: dict, resources: dict, chosen_drink: str) -> bool:
        """
        Function that validates if there are enough resources to prepare the ordered drink.
        ---
        Args:
            menu_dict (dict): Dictionary containing the available drinks with the required resources and their amounts.
            resources (dict): Dictionary containing the current machine's resources.
            chosen_drink (str): Drink that was ordered by the user.

        Returns:
            bool: True or False determining whether there are enough resources or not. If some resource is missing, it will also print out which one.
        """    
        #Initialize boolean variable for validation
        resource_validation = True
        
        #Check for required resources and compare their amount to the machine's resources
        for key, val in menu_dict[chosen_drink]["ingredients"].items():
            if val > resources[key]:
                resource_validation = False
                print(f"Sorry there is not enough {key}.")
                break
            
        return resource_validation

    #Function that process user's payment
    def process_coins(self, coin_dict: dict) -> float:
        """
        Function that asks the user to input coins for buying their drink, calculates and returns their balance in USD.
        ---
        Args:
            coin_dict (dict): Dictionary containing the different types of coins and their value in USD.

        Returns:
            float: User balance in USD after inserting coins.
        """    
        #Prompt for how many coins of each type are inserted into the machine
        q = int(input("How many quarters?"))
        d = int(input("How many dimes?"))
        n = int(input("How many nickels?"))
        p = int(input("How many pennies?"))
        
        input_balance = round((q * coin_dict["quarter"]) + (d * coin_dict["dime"]) + (n * coin_dict["nickel"]) + (p * coin_dict["penny"]), 2)
        
        return input_balance
    
    def validate_transaction(self, menu_dict: dict, resources: dict, chosen_drink: str, input_balance: float) -> bool:
        """
        Function that compares the user's balance with the price of the selected drink. If there is enough balance, completes order and takes profit.
        Also, validates if the user is receiving any change.
        ---
        Args:
            menu_dict (dict): Dictionary containing the available drinks with the required resources and their amounts.
            resources (dict): Dictionary containing the current machine's resources.
            chosen_drink (str): Drink that was ordered by the user.
            input_balance (float): User's balance in USD.

        Returns:
            bool: Returns *True* if transaction is completed, *False* if there was not enough money.
        """    
        #Initialize transaction status
        transaction_completed = False  
        
        #If there is enough balance, complete transaction and add profit to resources
        if input_balance >= menu_dict[chosen_drink]["cost"]:
            
            #If there is no change input_balance is higher than drink cost, refund
            if resources["money"] == 0 and input_balance > menu_dict[chosen_drink]["cost"]:
                print("There is no change in the machine. Please insert the exact amount.")
                return transaction_completed
            
            #If everthing is fine, add profit
            resources["money"] += menu_dict[chosen_drink]["cost"]
            
            #Validate if there is any change, and refund it if that is the case
            change = round(input_balance - menu_dict[chosen_drink]["cost"], 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
                
            #Complete transaction
            transaction_completed = True
            
    #If there is not enough money, refund and start over
        else:
            print("Sorry, that's not enough money. Money refunded.")
        return transaction_completed

    def make_coffee(self, menu_dict: dict, resources: dict, chosen_drink: str):
        """
        Function for deducting resources from the machine after making coffee, prints out a completed status for the user.
        ---
        Args:
            menu_dict (dict): Dictionary containing the available drinks with the required resources and their amounts.
            resources (dict): Dictionary containing the current machine's resources.
            chosen_drink (str): Drink that was ordered by the user.
        """    
        for key, val in menu_dict[chosen_drink]['ingredients'].items():
            resources[key] -= val

        print(f"Here is your {chosen_drink}. Enjoy! ☕")