"""
-------------------------------------------------------
[Lab 3, Task 7]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-01"
-------------------------------------------------------
"""
# Imports
from List_array import List
# Constants

key = [99]

target = List()

target.append([99])
target.append(99)

for x in target:
    print(x)

value = target.find(key)

print(value)