#Name: Richard Aguilar
#Date: May 30th, 2019
#This program: Draws an 8-sided polygon (octagon)

import turtle

richard = turtle.Turtle()
richard.color("purple")

for i in range(8):
    richard.forward(100)
    richard.left(360/8)

