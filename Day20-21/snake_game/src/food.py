from turtle import Turtle
import random

class Food(Turtle):
    '''
    Turtle object representing the food displayed in the screen for the snake game.
    '''
    
    #Initialize class and Turtle superclass
    def __init__(self):
        super().__init__()

        #Set food attributes
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5) #Modify turtle object to be 10x10 rather than 20x20 (default)
        self.color("white")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self) -> None:
        '''
        Make the food re-appear at a random location.
        '''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        return