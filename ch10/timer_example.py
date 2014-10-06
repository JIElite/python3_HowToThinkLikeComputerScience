import turtle

def move(tur_name):
    tur_name.forward(100)
    tur_name.left(56)




wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

while True:
    wn.ontimer(move(tess), 1000)

wn.mainloop()
