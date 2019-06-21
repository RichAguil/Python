#Name: Richard Aguilar
#Date: June 4th, 2019
#This program: Creates a spiral using turtle

import turtle

spiral = turtle.Turtle()

for i in range(0,100,10):
    spiral.forward(i)
    spiral.left(94)

