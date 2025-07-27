import turtle
import math

screen = turtle.Screen()
screen.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0,0)
t.pendown()
t.pensize(10)

for angle in range(360*3):
    r = angle * 0.5
    x = r * math.cos(math.radians(angle))
    y = r * math.sin(math.radians(angle))
    t.pencolor((angle % 255,100,200))
    t.goto(x,y)