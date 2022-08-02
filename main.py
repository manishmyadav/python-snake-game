from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
DELAY = 0.105

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()  # Creates a food at random place on the cordinate
scoreboard = Scoreboard()

screen.listen()  # To start listening for events

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(DELAY)  # After every 0.1 s
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) <= 15:
        print("Collision has occurred")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()























screen.exitonclick()