from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
RED = "#FF6666"
GREEN = "#00FF00"
WHITE = "#FFFFEE"
NUDE = "#FFDAB9"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Generating score label
        self.score_label = Label(text="Score : 0", background=THEME_COLOR, font=("Arial", 10, "bold"), fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Generating question card
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, 
            text="Sample Text", 
            fill=THEME_COLOR, 
            font=("Ariel", 20, "italic")
            )

        # Generate buttons
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_answer_for_false_and_get_score)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_answer_for_true_and_get_score)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg=WHITE)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg=NUDE)
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\nFinal score: {self.quiz.score}/{self.quiz.question_number}")

    def check_answer_for_false_and_get_score(self):
        self.give_feedback(is_true = self.quiz.check_answer("False"))

    def check_answer_for_true_and_get_score(self):
        self.give_feedback(is_true = self.quiz.check_answer("True"))


    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)