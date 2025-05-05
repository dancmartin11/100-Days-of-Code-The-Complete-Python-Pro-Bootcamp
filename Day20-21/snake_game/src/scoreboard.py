from turtle import Turtle

#Location (x,y) of the scoreboard
BOARD_LOC = (0, 280)
#Scoreboard font settings
ALIGN = "center"
FONT = "Arial"
SIZE = 14
TYPE = "normal"

class Scoreboard(Turtle):
    '''
    Creates and keeps track of the scoreboard displayed in the snake game.
    '''
    def __init__(self):
        super().__init__()
        self.score = 0
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
        self.write(f"Score: {self.score}", align = ALIGN, font = (FONT, SIZE, TYPE))    
        return
        
    def increase_score(self) -> None:
        '''
        Increase score when snake reaches food.
        '''
        self.score += 1
        self.update_scoreboard()
        return
    
    def game_over(self):
        '''
        Write a game over message when the user losses.
        '''
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGN, font = FONT)     
        return