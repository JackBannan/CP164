"""
-------------------------------------------------------
[Assignment 8]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-25"
-------------------------------------------------------
"""
# Imports

# Constants

from Letter import Letter
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    txt = file_variable.read()
    for i in txt:
        if i.isalpha():
            letter = Letter(i.upper())
            bst.retrieve(letter)

    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    a = bst.inorder()
    for i in a:
        total += i.comparisons
    return total
    

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = 1
    length = len("---------------------")
    a = bst.inorder()
    for i in a:
        total += i.count
    print("""Letter Count/Percent Table

Total Count: {:,}

Letter  Count       %
---------------------""".format(total))
    for letter in a:
        percen = float("{:.2f}".format(100*letter.count/total))
        print("    {}".format(letter.letter),end='')
        print(" "*(length - len(str(letter.count))-15),"{:,}".format(letter.count),end='')
        print(" "*(27-length-len(str(percen))), "{}%".format(percen))
    return