#Name: Richard Aguilar
#Date: June 20th, 2019
#This program:  Asks the user for an number and controls turtle based off of the input

import turtle

richard = turtle.Turtle()

number = int(input("Enter a whole number: "))

if number%2 == 0:
    richard.color('blue')
    richard.left(180)
    richard.forward(100)
else:
    richard.color('red')
    richard.forward(100)