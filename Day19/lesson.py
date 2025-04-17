#Import modules
from turtle import Turtle, Screen

#Generate turtle object and configure it
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue3")

#Initialize screen object
screen = Screen()

#Generate function to make tim the turtle move forward
def move_forward():
    tim.forward(10)

#Provide instructions using the screen object
screen.listen()
screen.onkey(
    key = "space",
    fun = move_forward #Function as input - does not require () HIGHER-ORDER FUNCTIONS
)
screen.exitonclick()