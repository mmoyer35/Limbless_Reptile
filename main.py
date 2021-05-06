from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Create the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Limbless reptile game!")
screen.tracer(0)

#Create the Limbless Reptile (aka snake), food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Set up screen, recieve the input buttons (Using the arrow keys)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Set up condition to keep the while loop running
game_is_on = True
while game_is_on:
    # Update and move the limbless reptile
    screen.update()
    time.sleep(.1)
    snake.move()
    # Check to see if the food was eaten, create new food at a random location if true, extend the reptile by one
    # segment, and add a point to the scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.eat()

    # Check to see if the reptile is still within the bounds of the screen. 20pixel buffer
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        food.refresh()
        scoreboard.reset()

    # Continuous check to make sure the reptile hasn't eaten itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            food.refresh()
            scoreboard.reset()

screen.exitonclick()
