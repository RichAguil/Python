#Name: Richard Aguilar
#Date: June 20th, 2019
#This program:  Greets a user based on time of day

hour = int(input ("Enter hour (in 24 hour time): "))

if hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")