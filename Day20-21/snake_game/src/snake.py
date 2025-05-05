#Import turtle module
from turtle import Turtle

#Set the starting position, movement distance for the snake and degrees for turning around
STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''
    Snake object for the snake game.
    '''
    def __init__(self, color):
        self.color = color
        #Create empty list which will later contain all the segments from the snake
        self.segments = []
        #Create the snake and define head (pointer that will guide the direction)
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        '''
        Creates the snake object.
        '''
        #Append initial positions to initialize snake
        for position in STARTING_POS:
            self.add_segment(position = position)     
        return
    
    def add_segment(self, position: tuple) -> None:
        '''
        Set and generate a new segment to extend the snake with the extend() function
        Args:
            position (tuple): Tuple with (x,y) coordinates of the new segment's position.
        '''
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        return
            
    def move(self) -> None:
        '''
        Makes the snake move forward once.
        '''
        #Iterate over each segment and follow the previous segment's position
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        #Move the first segment to the pointed direction
        self.segments[0].forward(MOVE_DISTANCE)
        return
        
    def up(self) -> None:
        '''
        Makes your turtle object move up.
        '''
        if self.head.heading() != DOWN: #Snake is not able to turn around the opposite way (otherwise it would crash with itself, and the user would lose)
            self.head.setheading(UP)
        return

    def down(self) -> None:
        '''
        Makes your turtle object move down.
        '''    
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  
        return
    
    def left(self) -> None:
        '''
        Makes your turtle object move left.
        '''    
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  
        return
    
    def right(self) -> None:
        '''
        Makes your turtle object move right.
        '''    
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)   
        return

    def extend(self) -> None:
        '''
        Add a new segment to the snake.
        '''
        self.add_segment(self.segments[-1].position())
        return