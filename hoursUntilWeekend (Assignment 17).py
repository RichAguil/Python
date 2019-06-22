#Name: Richard Aguilar
#Date: June 11th, 2019
#This program: Tells the user how many hours left until the weekend

hoursToWeekend = int(input("Enter number of hours: "))

if (hoursToWeekend < 24):
    print("Days: 0")
    print("Hours: " + str(hoursToWeekend))
else:
    days = hoursToWeekend//24
    hours = hoursToWeekend%24

    print("Days: " + str(days))
    print("Hours: " + str(hours))