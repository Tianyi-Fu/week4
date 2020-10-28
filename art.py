from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 9
        c = random() * 15 + 9
        d = l * (random() * 0.37 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n*0.2, n*0.7)
        circle(2)
        left(90)
    pu()
    backward(l)

bgcolor("white")
ht()
speed(0)
tracer(0, 0)
left(90)
pu()
backward(300)
tree(12, 100)
done()
