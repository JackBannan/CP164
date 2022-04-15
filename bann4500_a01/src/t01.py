"""
-------------------------------------------------------
[Assignment 1, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-13"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year
# Constants

year = int(input("Year: "))

leap_year = is_leap_year(year)

if leap_year == True:
    print("It is a leap year.")
else:
    print("It is not a leap year.")