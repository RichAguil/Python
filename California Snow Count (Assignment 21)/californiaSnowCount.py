#Name:  Richard Aguilar
#Date:  June 11th, 2019
#This program loads an image, counts the number of pixels that are nearly white as an estimate for snow pack.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt  
import numpy as np

filename = input('Enter file name: ')
ca = plt.imread(filename)   #Read in image
countSnow = 0            #Number of pixels that are almost white
t = 0.75                 #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for i in range(ca.shape[0]):
	for j in range(ca.shape[1]):
		if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
			countSnow = countSnow + 1

print("Snow count is", countSnow)