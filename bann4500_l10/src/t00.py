"""
-------------------------------------------------------
[Lab 1, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-29"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import create_randoms,create_sorted,create_reversed
# Constants

lists = create_randoms()

for i in lists:
    for x in i:
        print(x)
        
sor = create_sorted()
rev = create_reversed()


print("result sorted array: ")
for i in sor:
    print(i)
print("resulting reversed array: ")
for i in rev:
    print(i)
