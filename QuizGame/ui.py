from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=25, pady=25)

        self.score_label = Label(text="Score: 0",
                                 bg=THEME_COLOR,
                                 font=("Arial", 15, "normal"),
                                 fg="white")
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     font=("Arial", 16, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)

        correct_button_image = PhotoImage(file="./images/true.png")
        wrong_button_image = PhotoImage(file="./images/false.png")

        self.correct_button = Button(image=correct_button_image,
                                     highlightthickness=0,
                                     command=self.true_pressed)
        self.wrong_button = Button(image=wrong_button_image,
                                   highlightthickness=0,
                                   command=self.false_pressed)

        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.correct_button.grid(row=2, column=0, pady=20)
        self.wrong_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You are done")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)