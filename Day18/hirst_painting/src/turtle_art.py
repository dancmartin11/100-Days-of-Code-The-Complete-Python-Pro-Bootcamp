from turtle import Turtle
import random

def generate_hirst_painting(turtle: Turtle, colors: list, x_length: int, y_length: int) -> None:
    '''
    Generates a Damien Hirst-like painting using the Turtle module.
    
    Args:
        turtle (Turtle): Turtle object that will generate the painting.
        colors (list): List of RGB tuples which each represent a color (turtle.colormode MUST be set to 255)
        x_length (int): Number of dots that will be displayed in the X axis.
        x_length (int): Number of dots that will be displayed in the Y axis.
    '''
    
    #Set starting position, so that the painting can be aligned to the center
    turtle.penup()
    turtle.goto(-250, 250)
    turtle.hideturtle()

    #Generate the Damien Hirst painting
    for _ in range(y_length):
        for _ in range(x_length):
            turtle.dot(20, random.choice(colors))
            turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50 * x_length)
        turtle.right(180)

    return