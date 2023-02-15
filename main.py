import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#from startWindow import StartWindow
import turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = False
play = turtle.textinput("Start the game", "Press 'Y' to start the game")
if play.lower() == "y":
    game_is_on = True

    level = int(turtle.numinput("Select level", "enter number between 1 and 10", minval=1, maxval=10))
    difficulty = (11-level)/10
    print(difficulty)

else:
    turtle.color("white")
    turtle.write(f"click to exit")
    screen.exitonclick()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(difficulty)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
