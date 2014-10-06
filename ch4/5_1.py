import turtle

def mk_tur():
    tess = turtle.Turtle()
    tess.speed(0)
    return tess


def draw_part(t, size):
    for i in range(4):
        t.forward(size + i)
        t.right(90)


wn = turtle.Screen()
new_turtle = mk_tur()
size = 1

for i in range(20):
    draw_part(new_turtle, size)
    size = size + 4



wn.mainloop()



