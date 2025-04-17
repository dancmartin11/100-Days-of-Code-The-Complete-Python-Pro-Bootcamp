import random
from turtle import Turtle
class Commands():
    def __init__(self, turtle_object: Turtle):
        self.turtle_object = turtle_object
    
    #Generate function to make tim the turtle move forward
    def move_forward(self) -> None:
        '''
        Function that makes your turtle object move forward.
        '''
        self.turtle_object.forward(10)
        
    def move_back(self) -> None:
        '''
        Function that makes your turtle object move backwards.
        '''
        self.turtle_object.backward(10)
        
    def turn_left(self) -> None:
        '''
        Function that makes your turtle object turn left.
        '''
        self.turtle_object.left(10)
        
    def turn_right(self) -> None:
        '''
        Function that makes your turtle object turn right.
        '''
        self.turtle_object.right(10)
        
    def random_color(self) -> None:
        '''
        Function that randomly selects a color for the next Turtle's object's trace, based on an RGB tuple,
        which is accepted in the color change functions from the Turtle library.
        '''
        # Generate random integers in the range 1-255, then convert to the 0-1 range
        random_color = random.randint(1, 255) / 255, random.randint(1, 255) / 255, random.randint(1, 255) / 255
        self.turtle_object.color(random_color)
        return
        
    def restart(self) -> None:
        '''
        Function that makes your turtle go back to the origin and clear the screen.
        '''
        self.turtle_object.penup()
        self.turtle_object.clear()
        self.turtle_object.home()
        self.turtle_object.color('black')
        self.turtle_object.pendown()
        return