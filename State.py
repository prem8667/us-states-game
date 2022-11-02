from turtle import Turtle

class State(Turtle):

    def __init__(self, answer, x, y):
        super().__init__()
        self.hideturtle()
        self.answer = answer
        self.penup()

        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.write(self.answer)

