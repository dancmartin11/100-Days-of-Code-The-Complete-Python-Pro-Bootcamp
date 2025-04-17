#Import modules
from turtle import Turtle, Screen
import random

#Initialize and configure the screen object
screen = Screen()
screen.setup(width = 500, height = 400)

#Ask user to bet and create a list with turtle colors for participants
is_race_on = False
user_bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle will win the race? Enter a color: ").lower().strip()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#Generate the Turtle objects with each of the colors in the previous list and place them in the start line
turbo_turtles = {}
y_start = -150

for color in colors:
    turbo_turtles[color] = Turtle(shape = 'turtle')
    turbo_turtles[color].color(color)
    turbo_turtles[color].penup()
    turbo_turtles[color].goto(x = -240, y = y_start)
    
    y_start += 60

#Validate and start race
if user_bet:
    is_race_on = True

#Randomly make each turtle go forward until one of them reaches the goal (width of the screen)
while is_race_on:
    for turtle in turbo_turtles.values():
        #If turtle already won, end race and print result
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        #Move forward until one of them reaches the goal line            
        turtle.forward(random.randint(0,10))
    pass

#Set the exit on click option (click to close screen)
screen.exitonclick()