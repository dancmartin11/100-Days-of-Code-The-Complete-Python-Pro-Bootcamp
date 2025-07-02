# Import required modules
from turtle import Turtle

# Generate scoreboard constants
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        """
        Initialize the Scoreboard object, set the starting level, and display the scoreboard.
        """
        super().__init__()
        
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.display_scoreboard()
        
    def display_scoreboard(self):
        """
        Clear the previous scoreboard and write the current level at the top left of the screen.
        """
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)
        
    def increase_level(self):
        """
        Increase the level by 1 and update the scoreboard display.
        """
        self.level += 1
        self.display_scoreboard()
        
    def game_over(self):
        """
        Display the 'Game Over.' message at the center of the screen.
        """
        self.goto(0,0)
        self.write("Game Over.", align = "center", font = FONT)