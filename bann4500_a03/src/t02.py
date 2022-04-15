"""
-------------------------------------------------------
[Assignment 3, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-01"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants

stack = Stack()

source = [8,14,12,9,8,7,5]

array_to_stack(stack, source)

print("source")
print()
for s in stack:
    print(s)
print()


target1, target2 = stack.split_alt()

print("target1")
print()
for x in target1:
    print(x)
print()
print("target2")
print()
for y in target2:
    print(y)