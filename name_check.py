import pandas as pd
from turtle import Turtle
t = Turtle()
FONT = ("Courier", 8, "normal")


class NameCheck:
    def __init__(self, answer_state):
        data = pd.read_csv("50_states.csv")
        self.answer = data[data.state == answer_state].values.tolist()
        if not self.answer:
            pass
        else:
            new_x = self.answer[0][1]
            new_y = self.answer[0][2]
            arg = self.answer[0][0]
            t.hideturtle()
            t.penup()
            t.goto(new_x, new_y)
            t.write(arg=arg, align="center", font=FONT)
