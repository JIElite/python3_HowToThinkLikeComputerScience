import turtle

def mk_tur():
    tess = turtle.Turtle()
    tess.speed(0)
    return tess

def draw_star(t, size):
    for i in range(5):
        t.forward(size)
        t.left(144)

wn = turtle.Screen()
my_tur = mk_tur()
my_tur.left(36)
draw_star(my_tur, 100)

wn.mainloop()

