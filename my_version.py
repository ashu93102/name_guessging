import turtle as tur
import name_check
import pandas as pd

screen = tur.Screen()
screen.title("U.S. Game")

# Assigning image address to variable called image
image = "blank_states_img.gif"

# adding image to screen
screen.addshape(image)

# giving image to a turtle to show. Note image won't appear without assigning to turtle
# Turtle only works with gif image extension
tur.shape(image)

# guess = name_check.NameCheck()

screen.listen()

game_on = True
count = 0

while game_on:
    # answer_state = screen.textinput(title="Guess the state", prompt="What's another states name?").title()
    # data1 = pd.read_csv("50_states.csv")
    # answer = data1[data1.state == answer_state]
    # print(answer)
    count += 1
    answer_state = screen.textinput(title="Guess the state.", prompt=f"What's another states name?\nQuestion no. {count}/50").title()
    data1 = pd.read_csv("50_states.csv")
    name_check.NameCheck(answer_state)
    if count < 49:
        game_on = True
    else:
        game_on = False
