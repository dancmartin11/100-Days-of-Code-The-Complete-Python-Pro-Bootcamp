# Import required modules
from turtle import Turtle

# Constants for player (turtle) attributes
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Represents a player controlled turtle in the game."""
    
    def __init__(self, color):
        """
        Initialize the Player object with a given color, shape, and starting position.
        
        Args:
            color (str): The color of the player turtle.
        """
        super().__init__()
        
        self.color(color)
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90) # Face north
        
    def move_up(self):
        """
        Move the player forward by a fixed distance (upwards on the screen).
        """
        self.forward(MOVE_DISTANCE)
        
    def go_to_start(self):
        """
        Move the player back to the starting position at the bottom of the screen.
        """
        self.goto(STARTING_POSITION)
        
    def reached_finish_line(self):
        """
        Check if the player has reached the finish line at the top of the screen.
        
        Returns:
            bool: True if the player's y-coordinate is above the finish line, False otherwise.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
