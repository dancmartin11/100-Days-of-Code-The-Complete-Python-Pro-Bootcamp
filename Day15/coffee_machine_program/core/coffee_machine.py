# Import required libraries or modules
from core.machine_tasks import MachineTasks

# Initialize MachineTasks module
tasks = MachineTasks()

#Function that executes the whole process of the Coffee Machine
def CoffeeMachine(menu_dict: dict, coins_dict: dict, water_amount: int, milk_amount: int, coffee_amount: int, money_amount: float):
    """Main function that executes the full program of the Coffee Machine.

    Args:
        water_amount (int): Initial amount of water in ml.
        milk_amount (int): Initial amount of milk in ml.
        coffee_amount (int): Initial amount of coffee in ml.
        money_amount (float): Initial amount of money in USD (in case the machine needs to give change to the first customers).
    """
    # Initialize coffee machine
    turn_off = False

    # Initial resources
    machine_resources = {
        "water": water_amount,
        "milk": milk_amount,
        "coffee": coffee_amount,
        "money": money_amount,
    }

    # Run orders until machine gets turned off by maintenance staff
    while not turn_off:
        # Ask for users to input the drink they want
        drink = tasks.take_order(menu_dict=menu_dict)
        # Flow for users requesting drinks
        if drink != "off" and drink != "report":
            # Validate that there are enough resources in the machine
            enough_resources = tasks.check_resources(
                menu_dict=menu_dict, resources=machine_resources, chosen_drink=drink
            )
            if enough_resources:
                # Process coins input by the user and store their balance in USD
                print("Please insert coins.")
                user_balance = tasks.process_coins(coin_dict=coins_dict)

                # Validate if there is enough balance to process the transaction
                complete_transaction = tasks.validate_transaction(
                    menu_dict=menu_dict,
                    resources=machine_resources,
                    chosen_drink=drink,
                    input_balance=user_balance,
                )
                # If transaction was successfully completed, prepare coffee and deduct resources from machine (loop ends)
                if complete_transaction:
                    tasks.make_coffee(
                        menu_dict=menu_dict, resources=machine_resources, chosen_drink=drink
                    )

        # Flow for getting resource report
        elif drink == "report":
            print(tasks.get_report(machine_resources))
        # Flow for turning off the coffee machine

        else:
            turn_off = True
            print("Goodbye!")
