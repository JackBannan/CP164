"""
-------------------------------------------------------
[Lab 7, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-08"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()

lst.append(1)
lst.append(3)
lst.append(2)

key = 2

p, c, i = lst._linear_search_r(key)

print("p = {}, c = {}, i = {}".format(p,c,i))