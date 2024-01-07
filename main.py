import turtle as tur
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

# reading csv file using pandas
data = pd.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states Correct",
                                    prompt="What's another states name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("not_guessed.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = tur.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # .item() function look into data and print first itme from the data
        t.write(state_data.state.item())
