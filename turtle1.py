import time
import explorerhat
import turtle

turtle = None
screen = None
color = None
i = None

turtleDir = 59

def handle(ch,ev):
    if ev == 'pressed':
        turtleDir = turtleDir + 5
        print(turtleDir)




from turtle import *
turtle = Turtle()
screen = Screen()
screen.bgcolor(0, 0, 0)
color = ["red", "orange","yellow", "green", "blue", "purple"]
for i in range(360):
  turtle.color(color[i % 6])
  turtle.width(i / 100 + 1)
  turtle.forward(i)
  turtle.left(turtleDir)
  explorerhat.touch.pressed(handle)

