from turtle import Turtle
import os

#Location (x,y) of the scoreboard
BOARD_LOC = (0, 280)
#Scoreboard font settings
ALIGN = "center"
FONT = "Arial"
SIZE = 14
TYPE = "normal"
# Directory locations
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data.txt")

class Scoreboard(Turtle):
    '''
    Creates and keeps track of the scoreboard displayed in the snake game.
    '''
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(DATA_PATH, "r") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(BOARD_LOC)
        self.update_scoreboard()
        
    def update_scoreboard(self) -> None:
        '''
        Update the written output of the scoreboard.
        '''
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highest_score}", align = ALIGN, font = (FONT, SIZE, TYPE))    
        return
        
    def reset(self):
        '''
        Reset the score and validate if high score was surpassed, then save it into "data.txt"
        '''
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open(DATA_PATH, "w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self) -> None:
        '''
        Increase score when snake reaches food.
        '''
        self.score += 1
        self.update_scoreboard()