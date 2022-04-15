"""
-------------------------------------------------------
[Lab 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
# Constants

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        stack.push(source.pop())
    
    return 
    
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        target.insert(0,stack.pop())
    
    
    return
    
    
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    s = Stack()

    s.push(source.pop())
    
    b = s.is_empty()
    
    print(b)
    
    value = s.pop()
    
    print(value)
    
    s.push(source.pop())
    
    value = s.peek()
    
    print(value)
    
    return s
    
    
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        queue.insert(source.pop(0))
    
    return  

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    while not queue.is_empty():
        target.append(queue.remove())
    
    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        pq.insert(source.pop())
    
    return 

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        target.append(pq.remove())
    
    return 
    
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    
    print("Length of Queue (Initial): {}".format(len(q)))
    print("Length of a (Initial): {}".format(len(a)))
    
    while a != []:
        value = a[0]
        q.insert(value)
        a.remove(value)
        
    print("Length of Queue (Post insert): {}".format(len(q)))
    print("Length of a (Post removal): {}".format(len(a)))
    
    if q.is_empty() == False: #not empty queue
        print("Queue is not empty")
        value = q.peek()
        print("Peek: {}".format(value))
        n = len(q)
        print("Queue length: {}".format(n))
    else: #empty queue
        print("Queue is empty")
        n = len(q)
        print(n)
        
    # print the results of the method calls and verify by hand
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    
    print("Length of Queue (Initial): {}".format(len(pq)))
    print("Length of a (Initial): {}".format(len(a)))
    
    while a != []:
        value = a[0]
        pq.insert(value)
        a.remove(value)
        
    print("Length of Queue (Post insert): {}".format(len(pq)))
    print("Length of a (Post removal): {}".format(len(a)))
    
    if pq.is_empty() == False: #not empty queue
        print("Queue is not empty")
        value = pq.peek()
        print("Peek: {}".format(value))
        n = len(pq)
        print(n)
    else: #empty queue
        print("Queue is empty")
        n = len(pq)
        print(n)
        
    # print the results of the method calls and verify by hand
    return
    # print the results of the method calls and verify by hand
    
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        llist.insert(0,source.pop())
    
    return 

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not llist.is_empty():
        target.append(llist.pop(0))
    
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    print("Length of lst (Initial): {}".format(len(lst)))
    print("Length of source (Initial): {}".format(len(source)))
    
    key = source[0]
    
    while source != []:
        value = source[0]
        lst.insert(-1,value)
        source.remove(value)
        
    print("Length of lst (Post insert): {}".format(len(lst)))
    print("Length of source (Post removal): {}".format(len(source)))
    
    if lst.is_empty() == False: #not empty list
        print("Queue is not empty")
        value = lst.peek()
        print("Peek: {}".format(value))
        n = len(lst)
        print("Queue length: {}".format(n))
        value = lst.min()
        print("Min value: {}".format(value))
        value = lst.max()
        print("Max value")
        n = lst.index(key)
        print("Index of {} is {}".format(key,n))
        value = lst.find(key)
        print("Value = {}".format(value))
        n = lst.count(key)
        print("Key appears: {} times".format(n))
        lst.append(5)
        for x in lst:
            print(x)
        
    else: #empty list
        print("Queue is empty")
        n = len(lst)
        print(n)
    
    return
    