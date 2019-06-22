#Name: Richard Aguilar
#Date: June 11th, 2019
#This program: Converts binary to decimal

binString = input("Enter binary number: ")

decNum = 0


for char in binString:
    n = int(char)
    decNum = (decNum*2) + n

print (decNum)