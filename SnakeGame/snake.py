from turtle import Turtle
from random import randint, choice

SHAPE = "triangle"


class Snake:
    def __init__(self):
        self.snake = [Turtle(SHAPE), Turtle(SHAPE)]
        for turtle in self.snake:
            turtle.color("green")
            turtle.fillcolor("black")
            turtle.penup()
            turtle.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.snake[1].setx(-15)
        self.head = self.snake[0]
        self.head.fillcolor("green")

    def add_body(self):
        new_body = Turtle(SHAPE)
        new_body.penup()
        new_body.shapesize(stretch_wid=0.75, stretch_len=0.75)
        new_body.goto(self.snake[-1].position())
        new_body.color("green")
        new_body.fillcolor("black")
        self.snake.append(new_body)

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
        self.head.forward(15)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def teleport(self):
        if self.head.xcor() < -372:
            self.head.setx(372)
        elif self.head.xcor() > 372:
            self.head.setx(-372)
        elif self.head.ycor() > 248:
            self.head.sety(-248)
        elif self.head.ycor() < -248:
            self.head.sety(248)

    def restart(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.snake = [Turtle(SHAPE), Turtle(SHAPE)]
        for turtle in self.snake:
            turtle.color("green")
            turtle.fillcolor("black")
            turtle.penup()
            turtle.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.snake[1].setx(-15)
        self.head = self.snake[0]
        self.head.fillcolor("green")


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapes = ["circle", "turtle", "square", "triangle", "arrow", "classic"]
        self.colors = ["red", "green", "yellow", "cyan", "purple", "orange", "pink"]
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.update()

    def update(self):
        self.color(choice(self.colors))
        self.shape(choice(self.shapes))
        self.goto(randint(-340, 340), randint(-230, 230))


class Score(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open("highscore.txt") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            with open("highscore.txt", "w") as file:
                self.high_score = 0
                file.write("0")
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 210)

    def print_score(self):
        self.clear()
        self.write(f"Score : {self.score} High score : {self.high_score}", font=("Arial", 20, "normal"), align="center")

    def increase_score(self):
        self.score += 1

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.print_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", font=("Arial", 20, "normal"), align="center")


class Hurdle:
    def __init__(self):
        self.hurdles = []

    def add_hurdle(self):
        self.hurdles.append(Turtle("square"))
        self.hurdles[-1].color("red")
        self.hurdles[-1].fillcolor("white")
        self.hurdles[-1].penup()
        self.hurdles[-1].shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.hurdles[-1].goto(randint(-340, 340), randint(-230, 230))

    def restart(self):
        for hurdle in self.hurdles:
            hurdle.goto(1000, 1000)
        self.hurdles.clear()
