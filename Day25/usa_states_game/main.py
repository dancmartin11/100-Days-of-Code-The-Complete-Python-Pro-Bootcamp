# Import required modules
import turtle
import pandas as pd

# Define constants
IMAGE_PATH = "./images/blank_states_img.gif"
STATE_DATA_PATH = "./data/50_states.csv"
STATES_TO_LEARN_PATH = "./data/states_to_learn.csv"

# Initialize and configure turtle screen object
screen = turtle.Screen()
screen.title("U.S. States Game")
image = IMAGE_PATH
screen.addshape(image)
turtle.shape(image)

# Read state data into a DataFrame
df = pd.read_csv(STATE_DATA_PATH)

# Start the game
score = 0
correct_answers = []

while len(correct_answers) < 50:
    # Get answer from the user
    if score != 0:
        answer_state = screen.textinput(title = f"{score}/50 States Correct", prompt = "What is another state's name?") # Prompt box in screen object
    else:
        answer_state = screen.textinput(title = "Guess the State", prompt = "What is another state's name?") # Prompt box in screen object
        
    # Convert to title case    
    answer_state = answer_state.title()
    
    # Check for secret exit keyword
    if answer_state == "Exit":
        break
    
    # Check if the answer is correct and increase score
    if answer_state in df["state"].to_list() and answer_state not in correct_answers:
        
        # Create turtle object and write correct answer
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df["state"] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        
        # Append answer to correct answers and increase score
        correct_answers.append(answer_state)
        score += 1
        print(score)
        
# Generate CSV file with states that were not guessed correctly (in case exit keyword is used)
states_to_lean = df[~df['state'].isin(correct_answers)]
states_to_lean.to_csv(STATES_TO_LEARN_PATH, index = False)