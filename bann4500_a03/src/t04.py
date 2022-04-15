"""
-------------------------------------------------------
[Assignment 3, Task 4]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-04"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants

stack = Stack()

source = [1,2,3,4,5,6,7]

array_to_stack(stack, source)

print("stack")
print()
for s in stack:
    print(s)
print()

stack.reverse()

print()

print("Reverse stack")
print()
for s in stack:
    print(s)
print()