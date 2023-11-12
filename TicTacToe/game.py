from turtle import Turtle


class Game:
    def __init__(self):
        self.squares = [Turtle("square") for i in range(9)]
        for i in range(9):
            self.squares[i].penup()
            self.squares[i].shapesize(stretch_len=2.2, stretch_wid=2.2)
            self.squares[i].color("gray")

    def put_squares(self):
        self.squares[0].goto(-62, 60)
        self.squares[1].goto(0, 60)
        self.squares[2].goto(62, 60)
        self.squares[3].goto(-62, 0)
        self.squares[4].goto(0, 0)
        self.squares[5].goto(62, 0)
        self.squares[6].goto(-62, -60)
        self.squares[7].goto(0, -60)
        self.squares[8].goto(62, -60)

    def check_if_over(self):
        who_won = self.check_who_won()
        if who_won == "Draw":
            for square in self.squares:
                if square.xcor() % 1000 != 0 or square.xcor() == 0:
                    return False
            return True
        else:
            return True

    def check_who_won(self):
        if self.squares[0].xcor() == 1000 and self.squares[1].xcor() == 1000 and self.squares[2].xcor() == 1000:
            return "X"
        elif self.squares[3].xcor() == 1000 and self.squares[4].xcor() == 1000 and self.squares[5].xcor() == 1000:
            return "X"
        elif self.squares[6].xcor() == 1000 and self.squares[7].xcor() == 1000 and self.squares[8].xcor() == 1000:
            return "X"
        elif self.squares[0].xcor() == 1000 and self.squares[3].xcor() == 1000 and self.squares[6].xcor() == 1000:
            return "X"
        elif self.squares[1].xcor() == 1000 and self.squares[4].xcor() == 1000 and self.squares[7].xcor() == 1000:
            return "X"
        elif self.squares[2].xcor() == 1000 and self.squares[5].xcor() == 1000 and self.squares[8].xcor() == 1000:
            return "X"
        elif self.squares[0].xcor() == 1000 and self.squares[4].xcor() == 1000 and self.squares[8].xcor() == 1000:
            return "X"
        elif self.squares[2].xcor() == 1000 and self.squares[4].xcor() == 1000 and self.squares[6].xcor() == 1000:
            return "X"
        elif self.squares[0].xcor() == -1000 and self.squares[1].xcor() == -1000 and self.squares[2].xcor() == -1000:
            return "O"
        elif self.squares[3].xcor() == -1000 and self.squares[4].xcor() == -1000 and self.squares[5].xcor() == -1000:
            return "O"
        elif self.squares[6].xcor() == -1000 and self.squares[7].xcor() == -1000 and self.squares[8].xcor() == -1000:
            return "O"
        elif self.squares[0].xcor() == -1000 and self.squares[3].xcor() == -1000 and self.squares[6].xcor() == -1000:
            return "O"
        elif self.squares[1].xcor() == -1000 and self.squares[4].xcor() == -1000 and self.squares[7].xcor() == -1000:
            return "O"
        elif self.squares[2].xcor() == -1000 and self.squares[5].xcor() == -1000 and self.squares[8].xcor() == -1000:
            return "O"
        elif self.squares[0].xcor() == -1000 and self.squares[4].xcor() == -1000 and self.squares[8].xcor() == -1000:
            return "O"
        elif self.squares[2].xcor() == -1000 and self.squares[4].xcor() == -1000 and self.squares[6].xcor() == -1000:
            return "O"
        return "Draw"
