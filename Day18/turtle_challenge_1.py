#Import libraries
from turtle import Turtle, Screen

#Initialize the turtle object and configure it
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue3")

#Turtle Challenge 1 - Draw a Square
for i in range(1,5):
    tim.forward(100)
    tim.right(angle = 90)

#Prevent the screen from closing automatically after script finishes running
screen = Screen()
screen.exitonclick()