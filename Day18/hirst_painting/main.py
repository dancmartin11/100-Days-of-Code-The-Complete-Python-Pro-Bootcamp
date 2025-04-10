#Import libraries
from utils.image_utils import Image
from src.turtle_art import generate_hirst_painting
import turtle

#Set colormode to RGB tuples
turtle.colormode(255)

#Initialize image object and extract image colors
image = Image(image_path = 'docs/damien_hirst_painting.png')
colors = image.extract_colors(n_colors = 20)

#Delete white and clear image colors (those which are close to 245)
colors = sorted(colors)[:15]

#Initialize Turtle object and set attributes
leonardo = turtle.Turtle(shape  = 'turtle')
leonardo.color('DodgerBlue3')
leonardo.speed('fastest')

#Set starting position, so that the painting can be aligned to the center
generate_hirst_painting(
    turtle = leonardo,
    colors = colors,
    x_length = 10,
    y_length = 10
)

#Prevent the screen from closing automatically after script finishes running
screen = turtle.Screen()
screen.exitonclick()