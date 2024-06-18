import turtle
a = turtle.Turtle()
a.shape('turtle')
def draw_rectangle():
    for i in range(2):
        a.forward(100)
        a.right(90)
        a.forward(50)
        a.right(90)

def draw_colour_triangle():
    color = input('Enter the colour you want for your  triangle(red, orange, yellow, green, blue, cyan, purple, pink, magenta, light green, turquoise and light blue(spell the only on color corectly.)) : ')
    a.color(color)
    for i in range(3):
        a.forward(100)
        a.right(120)
