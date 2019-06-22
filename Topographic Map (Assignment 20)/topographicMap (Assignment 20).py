# Name: Richard Aguilar
# Date: June 11th, 2019
# Takes elevation data of NYC and displays using the default color map


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt('C:/Users/ryagu/OneDrive/Documents/Python Scripts/Topographic Map (Assignment 20)/elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0: 
            #Below sea level
            floodMap[row,col,2] = 0.5     #Set the blue channel to 50%

        elif elevations[row,col] == 1:
            #Below the storm surge of Hurricane Sandy (flooding likely)
            floodMap[row,col,0] = 0.75     #Set the red channel to 75%
            floodMap[row,col,1] = 0.75     #Set the green channel to 75%
            floodMap[row,col,2] = 0.75     #Set the blue channel to 75%

        else:
            #Above 20 feet
            floodMap[row,col,0] = 0.5   #Set the red channel to 50%
            floodMap[row,col,1] = 0.5   #Set the green channel to 50%
            floodMap[row,col,2] = 0.5   #Set the blue channel to 50%

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Display the plot:
plt.show()

#Save the image:
plt.imsave('floodMap.png', floodMap)