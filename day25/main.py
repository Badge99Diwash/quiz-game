from turtle import Turtle, Screen
import pandas
screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
t = Turtle()
t.shape(image)
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
user_enter_states = []
name = []
score = 0
while len(user_enter_states) < 50:

    user = screen.textinput(f"{len(user_enter_states)}", 'please enter the states name:').title()
    if user in name:
        user = screen.textinput(f"Invalid", 'you have already named this state:').title()
    if user in all_states:
        new_t = Turtle()
        new_t.hideturtle()
        new_t.penup()
        state_data = data[data.state == user]
        x = state_data.x
        y = state_data.y
        new_t.goto(int(x), int(y))
        new_t.write(user)
        user_enter_states.append(t)
        name.append(user)
screen.exitonclick()
