
import turtle


def make_turtle():
    t = turtle.Turtle()
    return t

def draw_square(turtle_name):
    for i in range(4):
        turtle_name.forward(20)
        turtle_name.left(90)
    turtle_name.penup()
    turtle_name.forward(40)
    turtle_name.pendown()




wn = turtle.Screen()
tess = make_turtle()

for i in range(5):
    draw_square(tess)
wn.mainloop()
