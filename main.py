import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=1250, height=800)
screen.title("Guess States")
image = "malaysia.gif"
screen.addshape(image)
turtle.shape(image)

## Setup game data
## Get x,y coordinate for each state
# coor = []
# def get_mouse_click_coor(x, y):
#     coordinate = x, y
#     coor.append(coordinate)
#     print(coordinate)
# df = pd.DataFrame(coor)
# df.to_csv("coordinate.csv")

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


correct_answer = []

game_is_on = True

while game_is_on:
    data = pd.read_csv('coordinate.csv')
    state = data.state.to_list()  # list of all states

    answer = screen.textinput(f"{len(correct_answer)}/{len(state)}", "Guess any states: ").title()
    # print(answer)

    #  check if answer is in all state list. if it exists, then print answer on the screen at its x,y coordinate
    if answer in state:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        df = data[data.state == answer]
        t.goto(int(df.x.iloc[0]), int(df.y.iloc[0]))
        t.write(answer, align='center', font=("Courier", 10, "bold"))
        correct_answer.append(answer)
        # print(correct_answer)

    # if all states guessed correctly, break loop and end the game
    if len(correct_answer) == len(state):
        game_is_on = False

    # if player give up on guessing state, exit game and create csv file of missing states
    if answer == "Exit":
        missing_state = []
        for s in state:
            if s not in correct_answer:
                missing_state.append(s)
        print(missing_state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv('missing_state')
        game_is_on = False


screen.exitonclick()
