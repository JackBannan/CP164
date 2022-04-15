"""
-------------------------------------------------------
[Lab 10, Task 3]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-29"
-------------------------------------------------------
"""
# Imports
from test_Sorts_array import test_sort,SORTS

# Constants

print("""n:   100       |      Comparisons       | |         Swaps          |
Algorithm      In Order Reversed   Random In Order Reversed   Random
-------------- -------- -------- -------- -------- -------- --------""")

for i in SORTS:
    title = i[0]
    func = i[1]
    test_sort(title, func)