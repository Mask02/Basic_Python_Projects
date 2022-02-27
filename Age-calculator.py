#!/usr/bin/python

import datetime


month_dict = {1:31,2:28,3:31,
		4:30,5:31,6:30,
		7:31,8:31,9:30,
		10:31,11:30,
		12:31}

def is_leap(year):
    leap = False


    if   year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True

    return leap

birth_day = int(input("Enter Your birth day :"))

birth_month = int(input("Enter your birth month :"))

birth_year = int(input("Enter your birth year :"))


x = datetime.datetime.now()

cYear = int(x.strftime("%Y"))

cMonth =int(x.strftime("%m"))

cDay = int(x.strftime("%d"))

leapDays = 0



if is_leap(birth_year):
	# Updating month_dict when birth year is leap year
	month_dict[2] = 29

	if birth_month > 2:
		leapDays = ((cYear - birth_year) / 4) - 1
	else:
		leapDays = ((cYear - birth_year) / 4)

else:

	l_year = birth_year

	for  x in range(4):
		
		l_year = l_year + 1

		if is_leap(l_year):
			leapDays = (cYear - l_year) / 4

if is_leap(cYear):
	if cMonth < 3 and cDay < 29:
		leapDays = leapDays - 1


year = (cYear - birth_year) - 1

month = (12 - birth_month) + cMonth

year = year + int(month/12)
 
month = month % 12

day = (month_dict[birth_month] - birth_day) + cDay

month = month + int(day/month_dict[birth_month])

day = day % month_dict[birth_month]

print("Your Age is: ", year, "Years", month, "Months", day, "Days")
