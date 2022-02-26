#!/usr/bin/python

import datetime

birth_day = int(input("Enter Your birth day :"))

birth_month = int(input("Enter your birth month :"))

birth_year = int(input("Enter your birth year :"))


x = datetime.datetime.now()
  
c_year = int(x.strftime("%Y")) - birth_year

print ("\n" + str(c_year), "Years",birth_month, "Months",birth_day, "Days")



