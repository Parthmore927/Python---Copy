import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()

radius = 100

for angles in range(360):
    x = radius* math.cos(math.radians(angles))
    y = radius* math.sin(math.radians(angles))
    t.goto(x,y)