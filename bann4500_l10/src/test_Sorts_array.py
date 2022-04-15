"""
-------------------------------------------------------
[Lab 10, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-26"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    
    
    
    for i in range(0,SIZE):
        values.append(Number(i))
        

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    
    for i in range(99,-1,-1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TEST rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    '''values = []'''
    
    arrays = []
    
    '''for x in range(0,TESTS):
        for i in range(0,SIZE):
            n = random.randint(0,XRANGE)
            values.append(Number(n))
        arrays.append(values)
        values = []'''
    
    for _ in range(TESTS):
        temp = random.sample(range(XRANGE), SIZE)
        values = []
        
        for i in range(SIZE):
            values.append(Number(temp[i]))
        arrays.append(values)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    Number.comparisons = 0
    Sorts.swaps = 0
    
    values = create_sorted()
    
    func(values)
    
    sorted_comparisons = Number.comparisons
    
    sorted_swaps = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    values2 = create_reversed()
    
    func(values2)
    
    reverse_comparisons = Number.comparisons
    
    reverse_swaps = Sorts.swaps
    
    Number.comparisons = 0
    Sorts.swaps = 0
    
    lists = create_randoms()
    
    for a in lists:
        func(a)
    
    random_comparisons = Number.comparisons // TESTS
    
    random_swaps = Sorts.swaps // TESTS
    
    print("{0:14} {1:>8} {2:>8} {3:>8} {1:>8} {2:>8} {3:>8}".format(title,sorted_comparisons,reverse_comparisons,random_comparisons,sorted_swaps,reverse_swaps,random_swaps))
       
    return
