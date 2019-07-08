import turtle
pen = turtle.Pen()
pen.speed(0)
pen.color("red","yellow")
pen.begin_fill()
for var in range(200):
    pen.forward(250)
    pen.left(171)
pen.end_fill()
turtle.exitonclick()
