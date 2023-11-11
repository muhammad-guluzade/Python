from turtle import Screen
from snake import Snake, Food, Score, Hurdle
from time import sleep

screen = Screen()
screen.setup(width=750, height=500)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

obstacles = Hurdle()
snake = Snake()
food = Food()
food_2 = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score.print_score()
screen.update()

game_on = True
aorn = False

while game_on:
    sleep(0.1)
    snake.move()
    screen.update()
    if snake.head.distance(food) < 15:
        aorn = True
        food.update()
        snake.add_body()
        score.increase_score()
        score.print_score()
    if snake.head.distance(food_2) < 15:
        aorn = True
        food_2.update()
        snake.add_body()
        score.increase_score()
        score.print_score()
    snake.teleport()
    for turtle in snake.snake[1:]:
        if snake.head.distance(turtle) < 10:
            score.restart()
            snake.restart()
            obstacles.restart()
            aorn = False
    if score.score % 5 == 0 and aorn:
        obstacles.add_hurdle()
        aorn = False
    for obstacle in obstacles.hurdles:
        if snake.head.distance(obstacle) <= 13:
            score.restart()
            snake.restart()
            obstacles.restart()
            aorn = False


screen.exitonclick()
