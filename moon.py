import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
t.speed(20)
for i in range(250):
    t.circle(100)
    t.lt(1)
    t.circle(100)
    t.lt(1)
