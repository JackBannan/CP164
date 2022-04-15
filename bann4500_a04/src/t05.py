"""
-------------------------------------------------------
[Assignment 4, Task 5]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants

pq = Priority_Queue()

pq.insert(1)
pq.insert(3)
pq.insert(5)
pq.insert(7)
pq.insert(9)

key = 5

target1, target2 = pq.split_key(key)

print("Higher priority")
for x in target1:
    print(x)
    
print("Lower Priority")
for x in target2:
    print(x)