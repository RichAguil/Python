#Name: Richard Aguilar
#Date: June 11th, 2019
#This program: Ask the user for 5 whole integers and draws something with it

import turtle
richard = turtle.Turtle()

for i in range(6):
    num = int(input("Enter a number: "))
    richard.left(num)
    richard.forward(100)