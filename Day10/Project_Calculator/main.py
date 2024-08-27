#CALCULATOR
from art import logo

#Add function
def add(n1, n2):
    return n1 + n2

#Substract function
def substract(n1, n2):
    return n1 - n2

#Multiply function
def multiply(n1, n2):
    return n1 * n2

#Divide function
def divide(n1, n2):
    return n1 / n2

#Power function
def power(n1, n2):
    return n1 ** n2

#Create dictionary to store operations
operations = {"+": add, "-": substract, "*": multiply, "/": divide, '**': power}

def calculator():
    print(logo)
  #Create the inputs for the operation numbers
    try:
        num1 = float(input("What's the first number?: "))
    except:
        print('Please enter a valid number.')
        calculator()
  
  #Show operation symbols
    for symbol in operations:
        print(symbol)
  
  #Generate while loop to make as many operations as the user wants
    exit = False
    while not exit:
        try:
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))

            #Create a function to call the operations
            call_operation = operations[operation_symbol]
        except:
            print(f"Please enter a valid number and symbol. Your current value is {num1}.")
            continue
        #Execute the operation and get new result
        if num2 == 0 and call_operation == divide:
            print(f"Cannot divide number by 0. Your current value is {num1}.")
            continue
        result = call_operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
  
        #Ask user if the calculation will continue
        should_continue = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type any other key to exit: ").lower()
    
        if should_continue == 'y':
            num1 = result
        elif should_continue == 'n':
            exit = True
            print(f"Your final result is {result}.\n")
            calculator() #Recursion, call a function to itself
        else:
            exit = True
            print(f"Your final result is {result}. Goodbye!")
            
#Execute calculator
calculator()