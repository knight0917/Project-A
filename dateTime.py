import datetime


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = datetime.date(year, month, day)

hour = int(input("Enter your birth hour: "))
minute = int(input("Enter your birth minute: "))
second = int(input("Enter your birth second: "))
time1 = datetime.time(hour, minute, second)



print(f"Your date: {date1}")
print(f"Your time: {time1}")


