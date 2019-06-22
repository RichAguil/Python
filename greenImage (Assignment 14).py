#Name: Richard Aguilar
#Date: June 4th, 2019
#This program: A program that accepts a .png file and outputs a copy of that image colored green


import turtle
import matplotlib.pyplot as plt
import numpy as np

inputFile = input("Enter name of the input file: ")
outputFile = input("Enter name of the output file: ")

image = plt.imread(inputFile)
plt.imshow(inputFile)
image2 = image.copy()
image2[:,:,1] = 0
plt.imshow(image2)
plt.imsave(outputFile, image2)

