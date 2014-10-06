import turtle

def mk_tur():
    tess = turtle.Turtle()
    tess.speed(0)
    return tess

def draw_star(t, star, size):
    for i in range(star):
        t.forward(size)
        t.left(180 - (180 / star))


def draw_big_star(t, star, size):
    for i in range(star):
        draw_star(t, star, size)
        t.penup()
        t.forward(size * 3.5)
        t.left(180 - (180 / star))
        t.pendown()


wn = turtle.Screen()
my_tur = mk_tur()
my_tur.left(0) #36 = 180 - (720 / star)
draw_big_star(my_tur, 31, 100)


wn.mainloop()

