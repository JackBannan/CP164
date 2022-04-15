"""
-------------------------------------------------------
[Assignment 4]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-11"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue
from Priority_Queue_array import Priority_Queue
# Constants

def queue_is_identical(source1, source2):
    """
    ----------------
    Determines whether two given queues are identical. Entries of
    source1 and source2 are compared and if all contents are identical
    and in the same order, returns True, otherwise returns False.
    Use: identical = queue_is_identical(source1, source2)
    ---------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        identical - True if source1 and source2 are identical, False otherwise.
            source1 and source2 are unchanged. (boolean)
    ---------------
    """
    
    n1 = len(source1)
    n2 = len(source2)
    x = 0
    array1 = []
    array2 = []
    identical = True
    
    if source1.is_empty() and source2.is_empty() == True:
        identical = True
    else:
        if n1 != n2:
            identical = False
        else:
            while x<n1 and identical != False:
                value1 = source1.remove()
                value2 = source2.remove()
                if value1 != value2:
                    identical = False
                else:
                    identical = True
                array1.append(value1)
                array2.append(value2) 
                x += 1
            array_to_queue(source1, array1)
            array_to_queue(source2, array2)
            
    
    return identical

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while len(source)>0:
        value = source.remove()
        if value<key:
            target1.insert(value)
        else:
            target2.insert(value)
    
    return target1, target2