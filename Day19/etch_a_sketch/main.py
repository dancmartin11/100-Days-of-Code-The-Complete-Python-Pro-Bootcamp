#Import modules
from turtle import Turtle, Screen
from src.Commands import Commands

#Generate turtle object and configure it
tim = Turtle()

#Initialize screen object
screen = Screen()

#Initialize commands object and set turtle to perform each of them
commands = Commands(turtle_object = tim)

#Provide instructions using the screen and commands objects
screen.listen()
screen.onkey(key = "w", fun = commands.move_forward)
screen.onkey(key = "s", fun = commands.move_back)
screen.onkey(key = "a", fun = commands.turn_left)
screen.onkey(key = "d", fun = commands.turn_right)
screen.onkey(key = "c", fun = commands.restart)
screen.onkey(key = 'r', fun = commands.random_color)

#Exit screen when user clicks
screen.exitonclick()