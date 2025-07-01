from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class to manage and display the scoreboard for the Pong game.
    Inherits from turtle.Turtle and handles score tracking, updating, and display.
    """
    
    def __init__(self, color):
        """
        Initialize the scoreboard with the given color.
        Sets up the turtle, initializes scores, and displays the initial scoreboard.
        
        Args:
            color (str): The color of the scoreboard text.
        """
        super().__init__()
        
        # Configure the scoreboard's attributes
        self.color(color)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """
        Clear and redraw the scoreboard with the current left and right scores.
        """
        # Clear previous scoreboard
        self.clear()
        
        # Left side score
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        
        # Right side score
        self.goto(100, 200)
        self.write(self.r_score, align = "center", font = ("Courier", 80, "normal"))
        self.write(self.r_score, align = "center", font = ("Courier", 80, "normal"))
        
    def l_point(self):
        """
        Increment the left player's score by 1 and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()
        
    def r_point(self):
        """
        Increment the right player's score by 1 and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()