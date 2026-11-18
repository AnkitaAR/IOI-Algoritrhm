city=input("Enter the city name: ")
temp=float(input("Enter the temperature in Celsius: "))

if temp>35:
    print("It's a hot day in", city)

if temp>25:
    print("It's a pleasant day in", city)
else:
    print("It's a cold day in", city)

if temp>30:
    print("It's a hot day in", city)
elif temp>20:
    print("It's a pleasant day in", city)
elif temp>10:
    print("It's a cool day in", city)
elif temp>0:
    print("It's a cold day in", city)

import calendar
import datetime
current_time=datetime.datetime.now()
print("Current date and time:", current_time)
print(calendar.calendar(current_time.year))