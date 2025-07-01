from turtle import Turtle

#Create Paddle blueprint with Turtle parent class
class Paddle(Turtle):
    """
    Represents a paddle in the Pong game, allowing vertical movement.
    Inherits from turtle.Turtle.
    """

    def __init__(self, coordinates: tuple, color: str):
        """
        Initialize the Paddle object with a given position and color.
        Args:
            coordinates (tuple): The (x, y) position to place the paddle.
            color (str): The color of the paddle.
        """
        super().__init__()
    
        #Configure paddle object's attributes
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid =5, stretch_len = 1)
        self.penup()
        self.goto(coordinates)

    #Move paddle up and down
    def go_up(self):
        """
        Move the paddle up by 20 units on the y-axis.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        """
        Move the paddle down by 20 units on the y-axis.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

