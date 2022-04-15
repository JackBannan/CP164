"""
-------------------------------------------------------
[Lab 1, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()

lst.append(33)
lst.append(44)
lst.append(66)
lst.append(55)
lst.append(22)
lst.append(11)

key = 22

value = lst.find(key)


print('Find')
print(value)

print('list')
for x in lst:
    print(x)