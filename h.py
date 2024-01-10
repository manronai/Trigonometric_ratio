import turtle

skk = turtle.Turtle()
count = 0
for i in range(1, 2*360):
    count = count + 0.02*i
    skk.forward(1)
    skk.left(1*0.7)