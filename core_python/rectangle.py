
import turtle
pen = turtle.Pen()
pen.color('gray','red')
pen.begin_fill()
for var in range(4):
    pen.forward(350)
    pen.left(90)
pen.end_fill()
turtle.exitonclick()
