#Name: Richard Aguilar
#Date: June 20th, 2019
#This program:  Opens up csv file and plots data

import matplotlib.pyplot as plt

import pandas as pd

borough = input("Enter borough name: ")
outputFilename = input("Enter output file name: ")
pop = pd.read_csv('nycHistPop.csv', skiprows=5)
pop['Fraction'] = pop[borough]/pop['Total']

#Create a plot of year versus fraction of pop. in borough (with labels):
pop.plot(x = 'Year', y = 'Fraction')
#plt.show()
#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(outputFilename)

#'C:/Users/ryagu/OneDrive/Documents/Python Scripts/Borough Fraction Plot (Assignment 26)/nycHistPop.csv'