import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.speed(20)
for i in range(6):
    for col in ("red", "magenta", "blue", "cyan", "green", "yellow"):
        t.color(col)
        t.circle(150)

        t.left(10)
t.hideturtle()
