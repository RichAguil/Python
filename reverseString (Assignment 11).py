#Name: Richard Aguilar
#Date: June 4th, 2019
#This program: Takes a string and prints it out in reverse

message = input("Enter a message: ")

for i in range(len(message),0, -1):
    print(message[i-1])
