from turtle import *
from random import randint

Dobbi = Turtle()
Harry = Turtle()
Mike = Turtle()

Dobbi.shape('turtle')
Harry.shape('turtle')
Mike.shape('turtle')

Dobbi.penup()
Dobbi.goto(-10,0)

Harry.penup()
Harry.goto(0,10)

Mike.penup()
Mike.goto(10,0)

Harry.left(90)
Dobbi.right(140)
Mike.right(20)

Harry.color('yellow')
Dobbi.color('green')
Mike.color('blue')

hideturtle()
exitonclick()