import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(600, 500)
p = turtle.Turtle()
p.color("white")
p.pensize(5)
p.shape("turtle")
p.penup()
p.goto(0, 100)
p.pendown()
n = 5
for _ in range(n):
    p.forward(200)
    p.right(144)
turtle.done()