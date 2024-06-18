import turtle
import random
a = turtle.Turtle()
a.shape('turtle')
def draw_rectangle():
    for i in range(2):
        a.forward(100)
        a.right(90)
        a.forward(50)
        a.right(90)

colors =["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink", "magenta", "light green", "light blue" , "turquoise"]
def draw_colour_triangle():
    a.color(random.choice(colors))
    for i in range(3):
        a.forward(100)
        a.right(120)

def get_random_colour():
    a.color(random.choice(colors))

while True:
    get_random_colour()
    draw_colour_triangle()
    a.left(5)
    draw_rectangle()
