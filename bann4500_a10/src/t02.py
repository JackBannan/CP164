"""
-------------------------------------------------------
[Assignment 10, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-04-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts


a = List()
b = [654, 67, 789, 678, 56, 34, 90]

for n in b:
    a.append(n)

Sorts.radix_sort(a)

print("sorted array: {}".format([x for x in a]))

