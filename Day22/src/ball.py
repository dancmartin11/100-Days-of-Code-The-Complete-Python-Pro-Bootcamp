from turtle import Turtle

class Ball(Turtle):
    """
    Represents the ball in the Pong game, handling movement, bouncing, and resetting.
    Inherits from turtle.Turtle.
    """
    
    def __init__(self, color):
        """
        Initialize the Ball object with a given color, shape, and starting attributes.
        Args:
            color (str): The color of the ball.
        """
        super().__init__()
        
        #Configure ball object's attributes
        self.color(color)
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        """
        Move the ball by updating its x and y coordinates based on its current direction.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        """
        Reverse the vertical direction of the ball (y-axis bounce).
        """
        self.y_move *= -1
        
    def bounce_x(self):
        """
        Reverse the horizontal direction of the ball (x-axis bounce) and increase its speed.
        """
        self.x_move *= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        """
        Reset the ball to the center of the screen, restore speed, and reverse direction.
        """
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()