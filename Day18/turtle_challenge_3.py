#Import libraries
from turtle import Turtle, Screen
import random

#Initialize the turtle object and configure it
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue3")

#Turtle Challenge 3 - Drawing Different Shapes

#Generate function that draws shape
def draw_shape(turtle: Turtle, n_sides: int) -> None:
    '''
    Function that draws a shape with a Turtle object based on the selected sides.
    
    Args:
        turtle (turtle.Turtle): Turtle object that will generate the shape.
        n_sides (int): Number of sides of the output shape (e.g. 3 -> triangle)
    '''
    for _ in range(n_sides):
        turtle.forward(100)
        turtle.right(360/n_sides)
        
# Generate function to get random color
def random_color() -> None:
    '''
    Function that randomly selects a color for the next Turtle's object's trace, based on an RGB tuple,
    which is accepted in the color change functions from the Turtle library.
    '''
    # Generate random integers in the range 1-255, then convert to the 0-1 range
    return (random.randint(1, 255) / 255, random.randint(1, 255) / 255, random.randint(1, 255) / 255)

#Iterate to generate triangle-decagon
for i in range(3,11):
    tim.color(random_color())
    draw_shape(tim, i)

#Prevent the screen from closing automatically after script finishes running
screen = Screen()
screen.exitonclick()