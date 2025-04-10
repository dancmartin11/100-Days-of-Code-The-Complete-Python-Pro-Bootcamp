#Import libraries
from turtle import Turtle, Screen
import random

#Initialize the turtle object and configure it
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue3")
tim.pensize(1)
tim.speed("fastest")

#Turtle Challenge 5 - Generating a Spirograph

# Generate function to get random color
def random_color() -> None:
    '''
    Function that randomly selects a color for the next Turtle's object's trace, based on an RGB tuple,
    which is accepted in the color change functions from the Turtle library.
    '''
    # Generate random integers in the range 1-255, then convert to the 0-1 range
    return (random.randint(1, 255) / 255, random.randint(1, 255) / 255, random.randint(1, 255) / 255)

#Generate function that performs a spirograph
def spirograph(turtle: Turtle, n_laps: int) -> None:
    '''
    Function that generates a spirograph with a given number of circles.
    
    Args:
        turtle (turtle.Turtle): Turtle object that will perform the random walk.
        n_laps (int): Number of laps that the spirograph will perform
    '''
    
    #Set initial rotation to 45 degrees (after first lap)
    rotation = 45
    
    #Iterate to perform the selected amount of movements
    for _ in range(n_laps):
        for _ in range(4):
            turtle.color(random_color())
            turtle.circle(100)
            turtle.right(90)
        turtle.right(90)
        turtle.right(rotation) #Turn around in random direction (West, East, North, South)
        
        #Reduce the angle rotation by 1 to create new traces in the spirograph
        rotation = rotation - 1

    return

#Dr. Angela Yu's solution for the spirograph
def spirograph_v2(turtle: Turtle, size_of_gap: int):
    '''
    Function that generates a spirograph with a given gap size in a single lap.
    
    Args:
        turtle (turtle.Turtle): Turtle object that will perform the random walk.
        size_of_gap (int): Size of the gap between each circle that is drawn (if 360, only one circle will be drawn)
    '''
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(tim.heading() + size_of_gap)

#Run spirograph
'''
spirograph(
    turtle = tim,
    n_laps = 50
)
'''
spirograph_v2(
    turtle = tim,
    size_of_gap = 90
)

#Prevent the screen from closing automatically after script finishes running
screen = Screen()
screen.exitonclick()