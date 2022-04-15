"""
-------------------------------------------------------
[Lab 5, Task 5]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-18"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome
# Constants

s = "AAa"

palindrome = is_palindrome(s)

if palindrome == True:
    print("Yes")
else:
    print("No")