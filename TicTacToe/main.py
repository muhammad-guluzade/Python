from drawer import Drawer
from turtle import Screen
from game import Game
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.listen()
screen.tracer(0)

SHAPE = "X"
SCORE_1 = 0
SCORE_2 = 0
PLAYER_1 = "X"
PLAYER_2 = "O"
TURN = "Player 1"


def change_shape():
    global SHAPE, TURN
    if SHAPE == "X":
        SHAPE = "circle"
    else:
        SHAPE = "X"
    if TURN == "Player 1":
        TURN = "Player 2"
    else:
        TURN = "Player 1"


def pressed_square_1(x, y):
    drawer.draw_shape(SHAPE, 1)
    if SHAPE == "X":
        game.squares[0].goto(1000, 1000)
    else:
        game.squares[0].goto(-1000, 1000)
    change_shape()


def pressed_square_2(x, y):
    drawer.draw_shape(SHAPE, 2)
    if SHAPE == "X":
        game.squares[1].goto(1000, 1000)
    else:
        game.squares[1].goto(-1000, 1000)
    change_shape()


def pressed_square_3(x, y):
    drawer.draw_shape(SHAPE, 3)
    if SHAPE == "X":
        game.squares[2].goto(1000, 1000)
    else:
        game.squares[2].goto(-1000, 1000)
    change_shape()


def pressed_square_4(x, y):
    drawer.draw_shape(SHAPE, 4)
    if SHAPE == "X":
        game.squares[3].goto(1000, 1000)
    else:
        game.squares[3].goto(-1000, 1000)
    change_shape()


def pressed_square_5(x, y):
    drawer.draw_shape(SHAPE, 5)
    if SHAPE == "X":
        game.squares[4].goto(1000, 1000)
    else:
        game.squares[4].goto(-1000, 1000)
    change_shape()


def pressed_square_6(x, y):
    drawer.draw_shape(SHAPE, 6)
    if SHAPE == "X":
        game.squares[5].goto(1000, 1000)
    else:
        game.squares[5].goto(-1000, 1000)
    change_shape()


def pressed_square_7(x, y):
    drawer.draw_shape(SHAPE, 7)
    if SHAPE == "X":
        game.squares[6].goto(1000, 1000)
    else:
        game.squares[6].goto(-1000, 1000)
    change_shape()


def pressed_square_8(x, y):
    drawer.draw_shape(SHAPE, 8)
    if SHAPE == "X":
        game.squares[7].goto(1000, 1000)
    else:
        game.squares[7].goto(-1000, 1000)
    change_shape()


def pressed_square_9(x, y):
    drawer.draw_shape(SHAPE, 9)
    if SHAPE == "X":
        game.squares[8].goto(1000, 1000)
    else:
        game.squares[8].goto(-1000, 1000)
    change_shape()


game = Game()
game.put_squares()
drawer = Drawer()
drawer.draw_field()
drawer.draw_who_is_who(PLAYER_1, PLAYER_2)
drawer.draw_score(SCORE_1, SCORE_2)
screen.update()

game.squares[0].onclick(pressed_square_1)
game.squares[1].onclick(pressed_square_2)
game.squares[2].onclick(pressed_square_3)
game.squares[3].onclick(pressed_square_4)
game.squares[4].onclick(pressed_square_5)
game.squares[5].onclick(pressed_square_6)
game.squares[6].onclick(pressed_square_7)
game.squares[7].onclick(pressed_square_8)
game.squares[8].onclick(pressed_square_9)

game_on = True

while game_on:
    sleep(0.1)
    drawer.draw_turn(TURN)
    if game.check_if_over():
        winner = "Draw"
        drawer.clean()
        if game.check_who_won() == "X":
            SCORE_1 += 1
            winner = "Player 1"
            SHAPE = "circle"
        elif game.check_who_won() == "O":
            SCORE_2 += 1
            winner = "Player 2"
            SHAPE = "X"
        drawer.draw_who_won(winner)
        screen.update()
        sleep(2)
        drawer.clean()
        game.put_squares()
        drawer.draw_field()
        drawer.draw_who_is_who(PLAYER_1, PLAYER_2)
        drawer.draw_score(SCORE_1, SCORE_2)
    screen.update()
screen.mainloop()

