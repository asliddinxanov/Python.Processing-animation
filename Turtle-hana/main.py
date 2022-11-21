import turtle
from turtle import *

color('deeppink', 'red')
title('xanovs art')
speed(0)
bgcolor('black')
r, g, b = 0, 0, 0

def flower():
    for i in range(190):
        begin_fill()
        circle(190-i, 90)
        left(90)
        circle(190-i, 90)
        left(110)

        if i > 16:
            begin_fill()
            color('deeppink', 'greenyellow')
        elif i > 32:
            begin_fill()
            color('deeppink', 'pink')
        else:
            end_fill()

flower()
turtle.home()
mainloop()