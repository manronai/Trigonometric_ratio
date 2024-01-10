import turtle
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("This is my screen title!")
skk = turtle.Turtle()
skk.pencolor('white')
skk.speed(1)
for i in range(360):
    skk.forward(100)
    skk.backward(100)
    skk.left(1)
skk.penup()
skk.left(45)
skk.forward(250)
skk.pendown()
for i in range(360):
    skk.forward(200)
    skk.backward(200)
    skk.left(1)




