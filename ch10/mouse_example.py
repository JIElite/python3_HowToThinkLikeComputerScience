import turtle


def move(x, y):
    tess.goto(x, y)
    wn.title("go click at {0}, {1}".format(x, y))

turtle.setup(400, 500)
wn = turtle.Screen()

tess = turtle.Turtle()
tess.shape("circle")


wn.onclick(move)

wn.mainloop()
