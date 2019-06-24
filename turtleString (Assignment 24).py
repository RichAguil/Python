#Name: Richard Aguilar
#Date: June 20th, 2019
#This program:  Takes input from the user and controls the turtle

import turtle

richard = turtle.Turtle()
myWin = turtle.Screen()
commands = input("Please enter a command string: ")

for ch in commands:
    if ch == 'F':
        richard.forward(50)
    elif ch == 'L':
        richard.left(90)
    elif ch == 'R':
        richard.right(90)
    elif ch == '^':
        richard.penup()
    elif ch == 'v':
        richard.pendown()
    elif ch == 'B':
        richard.backward(50)
    elif ch == 'S':
        richard.stamp()
    elif ch == 'l':
        richard.left(45)
    elif ch == 'r':
        richard.right(45)
    elif ch == 'p':
        richard.color('purple')