color = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink","magenta", "light green", "light blue"]

import random as r

import turtle
sheldon = turtle.Turtle()

steps = r.randrange(10,70)

degrees = r.randrange(10,350)

Shape = ['arrow' , 'blank' , 'circle' , 'classic' , 'square' , 'triangle' , 'turtle']
while True:
    colour = r.choice(color)
    sHape = r.choice(Shape)
    sheldon.forward(steps)
    sheldon.left(degrees)
    sheldon.color(colour)
    sheldon.shape(sHape)
