from turtle import Screen
from src.paddle import Paddle
from src.ball import Ball
from src.scoreboard import Scoreboard
import time

# Generate and configure game objects
screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(coordinates = (350, 0), color = "white")
l_paddle = Paddle(coordinates = (-350, 0), color = "white")
ball = Ball(color = "white")
scoreboard = Scoreboard(color = "white")

# Make paddle objects move when user does certain action
screen.listen()

#Right paddle's commands
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Left paddle's commands
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Start the game
game_is_on = True

try:
    while game_is_on:
        time.sleep(ball.move_speed) # Slow down each iteration so the ball moves slower
        screen.update()
        ball.move()
        
        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280: # Screen is 300x300
            ball.bounce_y()
            
        # Detect collision with paddles
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()
            
        # Detect when right paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
            
        # Detect when left paddle misses
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()
    
except Exception as e:
    # Handle window closed or other exceptions gracefully
    print(f"Game ended: {e}")

#Always exit on click
screen.exitonclick()