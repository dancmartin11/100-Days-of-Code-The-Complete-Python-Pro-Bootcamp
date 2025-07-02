# Import required modules
import time
from turtle import Screen
from src.player import Player
from src.car_manager import CarManager
from src.scoreboard import Scoreboard

# Generate the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Generate the Turtle game objects
player = Player(color = "green")
car_manager = CarManager()
scoreboard = Scoreboard()

# Make the player object move when user press the UP key
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate new car
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect user reaching finish line
    if player.reached_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        
# Exit game screen
screen.exitonclick()