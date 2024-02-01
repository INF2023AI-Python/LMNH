import turtle
import random

print("Hello World")

import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["blue","green","yellow","red","purple"]

for i in range(500):
 t.color(random.choice(colors))
 t.forward(1)
 t.right(30)
 t.backward(1)
 t.circle(i)

turtle.done()