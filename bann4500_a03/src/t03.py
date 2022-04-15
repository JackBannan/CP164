"""
-------------------------------------------------------
[Assignment 3, Task 3]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-01"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
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

stack_reverse(stack)

print()

print("Reverse stack")
print()
for s in stack:
    print(s)
print()