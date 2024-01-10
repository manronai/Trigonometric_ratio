import turtle
import time

skk = turtle.Turtle()
skk.speed(100)
angle = 0
skk.penup()
skk.left(90)
skk.forward(300)
skk.right(90)
skk.pendown()
a = 0

for i in range(5*360):
    if i%360==0 and i != 0:
        a += 1
        skk.right(90)
        skk.forward(57.29)
        skk.left(90)

    skk.forward(5-a)
    skk.right(1)

    
    

turtle.done()
