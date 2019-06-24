#Name: Richard Aguilar
#Date: June 20th, 2019
#This program:  Opens up csv file and plots data

import matplotlib.pyplot as plt

import pandas as pd

borough = input("Enter borough name: ")

#outputFilename = input("Enter output file name: ")
pop = pd.read_csv('nycHistPop.csv', skiprows=5)
print ("Average Population is :", pop[borough].mean())
print ("Maximum Population is :", pop[borough].max())