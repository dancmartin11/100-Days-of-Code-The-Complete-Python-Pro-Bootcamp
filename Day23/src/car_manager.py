# Import required modules
from turtle import Turtle
import random

# Constants for car attributes
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    A class to manage the cars in the turtle crossing game.
    Responsible for creating, moving, and updating the cars.
    """
    
    def __init__(self):
        """
        Initialize the CarManager with an empty list of cars and set the starting car speed.
        """
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        """
        Randomly create a new car and add it to the list of cars.
        The car is only created if a random chance condition is met, to control car frequency.
        The new car is placed at a random vertical position on the right edge of the screen.
        """
        
        # Generate a random chance to slow down the car generation a little bit (if cars are created on each iteration, it is almost impossible to cross)
        random_chance = random.randint(1,6)
        if random_chance == 1:
        
            # Initialize new car object with its attributes
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid = 1, stretch_len = 2) # n * original_length
            new_car.penup()
            new_car.color(random.choice(COLORS))
            
            # Generate the car at a random position in the vertical axis
            random_y = random.randint(-250, 250) # Leave some space in screen at the edges
            new_car.goto(360, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        """
        Move all cars in the list to the left by the current car speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        """
        Increase the speed of all cars to make the game more challenging.
        """
        self.car_speed += MOVE_INCREMENT