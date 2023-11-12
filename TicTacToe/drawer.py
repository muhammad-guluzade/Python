from turtle import Turtle


class Drawer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(width=5)
        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.penup()
        self.drawer.color("black")
        self.drawer.goto(-85, 240)

    def draw_field(self):
        self.color("black")
        self.goto(x=-30, y=-90)
        self.pendown()
        self.sety(90)
        self.penup()
        self.goto(x=30, y=-90)
        self.pendown()
        self.sety(90)
        self.penup()
        self.goto(x=90, y=-30)
        self.pendown()
        self.setx(-90)
        self.penup()
        self.goto(x=90, y=30)
        self.pendown()
        self.setx(-90)
        self.penup()

    def square_decider(self, square_num):
        if square_num == 1:
            return (-62, 40)
        elif square_num == 2:
            return (0, 40)
        elif square_num == 3:
            return (62, 40)
        elif square_num == 4:
            return (-62, -20)
        elif square_num == 5:
            return (0, -20)
        elif square_num == 6:
            return (62, -20)
        elif square_num == 7:
            return (-62, -80)
        elif square_num == 8:
            return (0, -80)
        elif square_num == 9:
            return (62, -80)

    def draw_shape(self, shape, square_num):
        self.goto(self.square_decider(square_num))
        self.pendown()
        if shape == "circle":
            self.color("blue")
            self.circle(20)
        else:
            self.color("red")
            self.penup()
            self.setx(self.xcor()+15)
            self.pendown()
            self.goto(self.xcor()-30, self.ycor()+40)
            self.penup()
            self.setx(self.xcor()+30)
            self.pendown()
            self.goto(self.xcor()-30, self.ycor()-40)
        self.penup()

    def draw_score(self,score_1, score_2):
        self.color("black")
        self.goto(x=-200, y=100)
        self.write(arg=f"{score_1}", font=("Arial", 30, "bold"))
        self.goto(x=200, y=100)
        self.write(arg=f"{score_2}", font=("Arial", 30, "bold"))

    def draw_who_is_who(self, player_1_shape, player_2_shape):
        self.goto(x=-240, y=200)
        self.write(arg=f"Player 1: {player_1_shape}", font=("Arial", 18, "bold"))
        self.goto(x=150, y=200)
        self.write(arg=f"Player 2: {player_2_shape}", font=("Arial", 18, "bold"))

    def clean(self):
        self.clear()
        self.drawer.clear()

    def draw_who_won(self, winner):
        self.goto(0, 100)
        self.penup()
        self.color("black")
        if winner == "Draw":
            self.write(arg=f"{winner}!", font=("Arial", 30, "bold"), align="center")
        else:
            self.write(arg=f"{winner} won!", font=("Arial", 30, "bold"), align="center")

    def draw_turn(self, turn):
        self.drawer.clear()
        self.drawer.write(arg=f"{turn} turn", font=("Arial", 25, "bold"))
