#Import libraries
from turtle import Turtle, Screen

#Initialize the turtle object and configure it
tim = Turtle()
tim.shape("turtle")
tim.color("DodgerBlue3")

#Turtle Challenge 2 - Draw a Dashed Line
for i in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

#Prevent the screen from closing automatically after script finishes running
screen = Screen()
screen.exitonclick()