#Import libraries
from turtle import Turtle, Screen
import random

#Initialize the turtle object and configure it
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue3")
tim.pensize(20)
tim.speed("fastest")

#Turtle Challenge 4 - Generating a Random Walk

# Generate function to get random color
def random_color() -> tuple:
    '''
    Function that randomly selects a color for the next Turtle's object's trace, based on an RGB tuple,
    which is accepted in the color change functions from the Turtle library.
    '''
    # Generate random integers in the range 1-255, then convert to the 0-1 range
    return (random.randint(1, 255) / 255, random.randint(1, 255) / 255, random.randint(1, 255) / 255)

#Generate function that performs a random walk
def random_walk(turtle: Turtle, n_iters: int) -> None:
    '''
    Function that generates a random walk for a Turtle object to generate a random drawing.
    
    Args:
        turtle (turtle.Turtle): Turtle object that will perform the random walk.
        n_iters (int): Number of random moves that the turtle will perform.
    '''   
    #Generate a list that will determine the rotation of the Turtle object after each move
    watch = [0, 90, 180, 270]
    
    #Iterate to perform the selected amount of movements
    for _ in range(n_iters):            
        turtle.color(random_color())
        turtle.forward(random.randint(10,50))
        turtle.setheading(random.choice(watch)) #Turn around in random direction (West, East, North, South)
    return
        
#Run random walk
random_walk(
    turtle = tim,
    n_iters = 1000
    )

#Prevent the screen from closing automatically after script finishes running
screen = Screen()
screen.exitonclick()