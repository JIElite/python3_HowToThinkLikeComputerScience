import turtle
import random

def mk_turtle():
    t = turtle.Turtle()
    t.speed(1)
    t.color("blue", "red") # line color, fill color
    return t

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  " + str(height))
    t.right(90)
    t.forward(40) #width
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10) #each bar between another
    t.pendown()


data = []
for i in range(10):
    data.append(random.randint(60,100))


wn = turtle.Screen()
my_tur = mk_turtle()
my_tur.penup()
my_tur.forward(-200)
my_tur.pendown()



for i in data:
    draw_bar(my_tur, i)

wn.mainloop()

