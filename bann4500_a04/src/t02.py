"""
-------------------------------------------------------
[Assignment 4, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-11"
-------------------------------------------------------
"""
# Imports
from functions import queue_is_identical
from Queue_array import Queue
# Constants


queue1 = Queue()
queue2 = Queue()

queue1.insert(1)
queue2.insert(1)
queue1.insert(2)
queue2.insert(2)
queue1.insert(3)
queue2.insert(3)


identical = queue_is_identical(queue1, queue2)

if identical == True:
    print("True")
else:
    print("False")