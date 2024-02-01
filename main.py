import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(5)

colors = ["red", "blue", "purple", "green", "orange", "yellow", "pink", "brown", "gray"]

for i in range(500):
    t.color(random.choice(colors))
    t.forward(i) 
    t.right(61) 

turtle.done()