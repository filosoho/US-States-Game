import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_on = True
while game_on:
    if len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            t.goto(0, 300)
            t.write(f"Better luck next time! 🍀🤞🏼", align="center", font=("Courier", 18, "bold"))
            game_on = False
        if answer_state in all_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(answer_state)
    elif len(guessed_states) == 50:
        t.goto(0, 300)
        t.write(f"Whoo-hooo!🎉🥳\nYou guessed all the states!!🤓 👯🥇🏆", align="center", font=("Courier", 18, "bold"))
        game_on = False

screen.exitonclick()
