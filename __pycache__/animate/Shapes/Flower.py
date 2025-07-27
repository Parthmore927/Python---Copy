import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.goto(0,0)
t.pendown()
t.pensize(5)
t.speed(0)
t.hideturtle()
screen.bgcolor("black")
screen.colormode(255)

for angle in range(360 * 2):
    r = 100* math.sin(math.radians(angle * 5))
    x = r* math.cos(math.radians(angle))
    y = r* math.sin(math.radians(angle))
    t.pencolor(angle % 255,100,200)
    t.goto(x,y)

bg = turtle.Turtle()
bg.speed(0)
bg.hideturtle()
bg.penup()
screen.colormode(255)

