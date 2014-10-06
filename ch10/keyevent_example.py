import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("handle keypress")

tess = turtle.Turtle()


def go_forward():
    tess.forward(30)


def turn_left():
    tess.left(45)


def turn_right():
    tess.right(45)

def close_window():
    wn.bye()


wn.onkey(go_forward, "Up")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(close_window, "q")

wn.listen()
wn.mainloop()
