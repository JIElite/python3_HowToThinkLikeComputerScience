import turtle

def mk_turtle():
    t = turtle.Turtle()
    return t



def draw_square(tur_name):
    for i in range(4):
        tur_name.forward(50)
        tur_name.right(90)


wn = turtle.Screen()
tess = mk_turtle()
tess.left(90)
tess.speed(10)


for i in range(20):
    draw_square(tess)
    tess.right(360 / 20)

wn.mainloop()

