import turtle
import pandas
from State import State



screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

guessed_states = []
all_states = data.state.to_list()

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50", prompt="What's the another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        missing_list = pandas.DataFrame(missing_states)
        missing_list.to_csv("New_list")
        break
    for i in data.state:
        if answer_state == i:
            coord_x = data[data["state"] == answer_state]
            guessed_states.append(answer_state)

            x_cor = int(coord_x["x"])



            y_cor = int(coord_x["y"])


            state = State(answer_state, x_cor, y_cor)



screen.addshape















