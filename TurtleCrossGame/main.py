from turtle import Turtle, Screen
from time import sleep
from random import randint

STEP = 5
LEVEL = 1


def write_lvl():
    global LEVEL
    writer.clear()
    writer.write(arg=f"Level: {LEVEL}", font=("Arial", 30, "normal"), align="center")
    LEVEL += 1


def hide_all_cars():
    for car in cars_list:
        if player.distance(car) < 20:
            continue
        car.hideturtle()


def check_if_passed():
    if player.ycor() > 300:
        return True
    else:
        return False


def write_using_player(what_to_write):
    prev_cor = player.pos()
    player.goto(0, 0)
    player.pencolor("black")
    player.write(arg=what_to_write, font=("Arial", 30, "normal"), align="center")
    player.goto(prev_cor)
    player.pencolor("green")


def check_if_hit():
    for turtle_ in cars_list:
        if player.distance(turtle_) < 17:
            return True
    return False


def go(heading):
    if 300 > player.xcor() > -300:
        player.setheading(heading)
        player.forward(20)
    elif player.xcor() >= 300:
        player.setx(player.xcor()-20)
    elif player.xcor() <= -300:
        player.setx(player.xcor()+20)


def move_turtles():
    for turtle_ in cars_list:
        if turtle_.xcor() < -400:
            turtle_.goto(randint(400, 900), randint(-250, 250))
            while check_if_close(turtle_):
                turtle_.goto(randint(400, 600), randint(-250, 250))
        turtle_.backward(STEP)


def check_if_close(turtle_):
    for object_ in cars_list:
        if turtle_.distance(object_) < 30 and object_ != turtle_:
            return True
    return False


screen = Screen()
screen.screensize(600, 600)
screen.colormode(255)
screen.tracer(0)
screen.bgcolor("cyan")

screen.listen()
screen.onkeypress(lambda heading=90: go(heading), key="Up")
screen.onkeypress(lambda heading=270: go(heading), key="Down")
screen.onkeypress(lambda heading=180: go(heading), key="Left")
screen.onkeypress(lambda heading=0: go(heading), key="Right")

player = Turtle("turtle")
player.color("green")
player.penup()
player.setheading(90)
player.goto(0, -280)

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")
writer.goto(-300, 260)

cars_list = []
for i in range(35):
    turtle = Turtle("square")
    turtle.shapesize(stretch_len=2)
    turtle.penup()
    turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.goto(randint(300, 1100), randint(-250, 250))
    while check_if_close(turtle):
        turtle.goto(randint(300, 800), randint(-250, 250))
    cars_list.append(turtle)

game_on = True
write_lvl()

while game_on:
    move_turtles()
    if check_if_hit():
        hide_all_cars()
        write_using_player("Game Over")
        game_on = False
    if check_if_passed():
        player.goto(0, -280)
        STEP += 0.5
        write_lvl()
    screen.update()
    sleep(0.05)

screen.exitonclick()
