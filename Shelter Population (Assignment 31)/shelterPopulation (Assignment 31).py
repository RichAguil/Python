#Name: Richard Aguilar
#Date: June 20th, 2019
#This program: Makes a plot of total population that are children over time

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

homeless = pd.read_csv(inputFile)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Children")

#plt.show()

fig = plt.gcf()
fig.savefig(outputFile)

#'C:/Users/ryagu/OneDrive/Documents/Python Scripts/Shelter Population (Assignment 31)/DHS_Daily_Report.csv'
