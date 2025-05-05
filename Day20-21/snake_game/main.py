#Import required modules
from turtle import Screen
from src.snake import Snake
from src.food import Food
from src.scoreboard import Scoreboard
import time

#Initialize the screen object
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Starving Viper")
screen.tracer(0)

#Create snake object
viper = Snake(color = "red")
food = Food()
score = Scoreboard()

#Listen to user commands
screen.listen()
screen.onkey(viper.up, "Up")
screen.onkey(viper.down, "Down")
screen.onkey(viper.left, "Left")
screen.onkey(viper.right, "Right")
     
#Initialize the game   
exit_game = False
while not exit_game:
    #Update the screen every time a whole snake's movement is captured
    screen.update()
    time.sleep(0.1)
    
    #Execute function to make the snake move
    viper.move()
    
    #Detect collision with food
    if viper.head.distance(food) < 15: #Check distance in pixels between viper and food objects
        food.refresh()
        score.increase_score()
        viper.extend()
        print("nom nom nom")
    
    #Detect collision with walls
    if viper.head.xcor() > 280 or viper.head.xcor() < -280 or viper.head.ycor() > 280 or viper.head.ycor() < -280:
        exit_game = True
        score.game_over()
    
    #Detect collision with tail
    for segment in viper.segments[1:]:
        if viper.head.distance(segment) < 10:
            exit_game = True
            score.game_over()
    
screen.exitonclick()