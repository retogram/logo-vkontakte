from inspect import EndOfBlock
from turtle import *

bgcolor("#ffffff")
pencolor("#1a76fd")
pensize(10)

penup()
goto(145, -60)
pendown()

begin_fill()
fillcolor("#1a76fd")
left(90)
for i in range(4):
    forward(167)
    circle(72, 90)
end_fill()

penup()
goto(-105, 80)
pencolor("#ffffff")
pensize(35)
pendown()

right(180)
circle(120, 75)
left(105)
forward(120)

penup()
goto(-5, 25)
pendown()

right(90)
circle(83, 75)

penup()
goto(-5, 25)
pendown()

right(75)
circle(-86, 75)

done()
hideturtle()
